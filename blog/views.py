from django.shortcuts import render , redirect , get_object_or_404
from user_profile.models import UserProfile
from .models import Post, Category, Comment
from .form import PostForm, CommentForm
from account.models import Account, ProfileImage, Bio, BackgroundImage, Advertisement
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages



# Create your views here.
@login_required(login_url='login_page')
def home(request, category_slug=None):
    category = None
    profile = UserProfile.objects.filter(user=request.user)  
    
    
    posts = Post.objects.all()
    categories = Category.objects.all()
    ads = Advertisement.objects.get()
    
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)
    
    return render(request, 'blog/home.html',{
        'profile':profile,
        'posts':posts,
        'categories':categories,
        'category':category,
        'ads':ads
        })



@login_required(login_url='login_page')
def post(request):
    if request.user.has_profile:
        form = PostForm()
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                
                return redirect('home_page')

        return render(request, 'blog/post.html', {'form': form})
    else:
        return redirect('update_profile_page')



@login_required(login_url='login_page')
def read_post(request, pk):
    
    post = get_object_or_404(Post, id=pk)
    
    return render(request, 'blog/read_post.html',{'post':post})



@login_required(login_url='login_page')
def about_user(request, username):
    user = get_object_or_404(Account, username=username)

    posts = Post.objects.filter(user=user)
    
    user_image = ProfileImage.objects.filter(user=user).first()
    
    user_background = BackgroundImage.objects.filter(user=user).first()
    
    user_bio = Bio.objects.filter(user=user).first()


    return render(request, 'blog/about_user.html', {
        'user': user,
        'posts': posts,
        'user_image':user_image,
        'user_background':user_background,
        'user_bio':user_bio
    })
    


@login_required(login_url='login_page')
def edit_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    
    if post.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user 
            post.save()
            
            messages.success(request, "Your post has been updated successfully!")
            return redirect('about-user', post.user.username)
    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
        'post': post
    }
    
    return render(request, 'blog/edit_post.html', context)






@login_required(login_url='login_page')
def delete_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    
    if post.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")
    
    if request.method == 'POST':
        post.delete()
        
        return redirect('about-user', post.user.username)
        
    return render(request, 'blog/delete_post.html')


@login_required(login_url='login_page')
def comment(request, pk):
    post = get_object_or_404(Post, id=pk)
    ads = Advertisement.objects.get()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            
            instance.user = request.user
            instance.post = post
            
            instance.save()
        return redirect('comment', post.id)
    else:
        comment_form = CommentForm()
    
    
    context = {
        'post':post,
        'comment_form':comment_form,
        'ads':ads
    }
    
    return render(request, 'blog/comment.html',context)
     





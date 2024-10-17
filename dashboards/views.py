from django.shortcuts import render, get_object_or_404, redirect
from account.models import Bio, Account, ProfileImage, BackgroundImage
from blog.models import Post
from django.contrib.auth.decorators import login_required
from account.form import ProfilePicForm, BackgroundForm, BioForm



# Create your views here.
@login_required(login_url='login_page')
def dashboard(request):
    
    user_name = request.user
    posts = Post.objects.filter(user=request.user)
    user_image = ProfileImage.objects.filter(user=request.user).first()
    user_background =BackgroundImage.objects.filter(user=request.user).first()
    user_bio = Bio.objects.filter(user=request.user).first()
    
        
    context = {
        'user_name': user_name,
        'posts':posts,
        'user_image':user_image,
        'user_background':user_background,
        'user_bio':user_bio
    }
    
    return render(request, 'dashboards/dashboard.html', context)

@login_required(login_url='login_page')
def upload_profile(request):
    profile_image = get_object_or_404(ProfileImage, user=request.user)
    background_images = get_object_or_404(BackgroundImage, user=request.user)
    bio = get_object_or_404(Bio, user=request.user)
    
    profile_form = ProfilePicForm(instance=profile_image)
    background_form = BackgroundForm(instance=background_images)
    bio_form = BioForm(instance=bio)

    if request.method == 'POST':
        if 'profile_submit' in request.POST:
            profile_form = ProfilePicForm(request.POST, request.FILES, instance=profile_image)
            if profile_form.is_valid():
                var = profile_form.save(commit=False)
                var.user = request.user
                var.save()
                return redirect('profile-upload')

        elif 'background_submit' in request.POST:
            background_form = BackgroundForm(request.POST, request.FILES, instance=background_images)
            if background_form.is_valid():
                var2 = background_form.save(commit=False)
                var2.user = request.user
                var2.save()
                return redirect('profile-upload')

        elif 'bio_submit' in request.POST:
            bio_form = BioForm(request.POST, instance=bio)
            if bio_form.is_valid():
                var3 = bio_form.save(commit=False)
                var3.user = request.user
                var3.save()
                return redirect('user-dashboard')
    
    context = {
        'profile_form': profile_form,
        'background_form': background_form,
        'bio_form': bio_form,
        'profile_image': profile_image,
        'background_images': background_images,
        'bio': bio,
    }      
    return render(request, 'dashboards/upload_profile.html', context)

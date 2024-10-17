from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from .form import RegistrationForm
from user_profile.models import UserProfile
from django.contrib import messages


# Create your views here.
def login(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('home_page')
        
        else:
            messages.warning(request, 'incorrect username or password')
            return redirect('login_page')
    return render(request, 'account/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login_page')





def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            var = form.save(commit=False)
            var.save()
            
            UserProfile.objects.create(user=var)
            
            messages.info(request, 'your account have been created successfully')
            return redirect('login_page')
        
        else:
            messages.error(request, 'something went wrong')
            return redirect('register_page') 
    
    else:
        form =  RegistrationForm(request.POST)
    return render(request, 'account/register.html',{'form':form})




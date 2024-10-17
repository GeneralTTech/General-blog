from django.shortcuts import render ,get_object_or_404, redirect
from .form import UpdateForm
from .models import UserProfile
from account.models import Account

from django.contrib.auth.decorators import login_required






# Create your views here.
@login_required(login_url='login_page')
def update_profile(request):
    profiles = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES, instance=profiles)
        if form.is_valid():
            form.save()
            
            user = Account.objects.get(id=request.user.id)
            user.has_profile = True
            user.save()
            
            return redirect('user-dashboard')
    else:
        form = UpdateForm(instance=profiles)
            
    return render(request, 'user_profile/update_profile.html', {'form':form, 'profile':profiles})


def about_(request):
    return render(request, 'user_profile/about_.html')
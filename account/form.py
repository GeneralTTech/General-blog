from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from .models import ProfileImage, BackgroundImage, Bio

class RegistrationForm(UserCreationForm):
    class Meta():
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')



class ProfilePicForm(ModelForm):
    class Meta():
        model = ProfileImage
        fields = ('profile_picture',)


class BackgroundForm(ModelForm):
    class Meta():
        model = BackgroundImage
        fields = ('background_image',)


class BioForm(ModelForm):
    class Meta():
        model = Bio
        fields = ('bio',)



from .models import UserProfile
from django.forms import ModelForm

class UpdateForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
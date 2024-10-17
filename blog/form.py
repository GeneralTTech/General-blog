from django.forms import ModelForm
from .models import Post, Comment
from account.models import ProfileImage


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('user',)
        
        

class ProfileImageForm(ModelForm):
    class Meta:
        model = ProfileImage
        fields = '__all__'
        
        
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
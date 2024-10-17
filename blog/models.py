from django.db import models
from user_profile.models import UserProfile
from tinymce.models import HTMLField
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from account.models import Account



# Create your models here.
class Category(models.Model):
    Category = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name_plural ='Categories'
    
    def __str__(self):
        return self.Category 
    

class Post(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = HTMLField()
    image = models.ImageField(upload_to='post_image', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        ordering = ('-created',)
        
    def comment_count(self):
        return self.comment_set.all().count()
    
    def comments(self):
        return self.comment_set.all()
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    
    def __str__(self):
        return self.user.username

    
    
  
    
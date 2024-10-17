from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify


# Create your models here.
class Account(AbstractUser):
    has_profile = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True, null=True)  # Add SlugField

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)
    

class ProfileImage(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_image', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])],)
    
    
    def __str__(self):
        return self.user.username
    
class BackgroundImage(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    background_image = models.ImageField(default='defaults.jpg', upload_to='profile_image', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])],)
    
    def __str__(self):
        return self.user.username
    
    

class Bio(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    bio = models.TextField()
    
    def __str__(self):
        return self.user.username

class Advertisement(models.Model):
    image1 = models.ImageField(upload_to='Ads_image', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])],)
    image2 = models.ImageField(upload_to='Ads_image', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])],)
    
    
    
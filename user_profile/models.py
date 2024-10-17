from django.db import models
from django.core.validators import FileExtensionValidator
from account.models import Account




# Create your models here.
class UserProfile(models.Model):
    gender_choice = {
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('None', 'None')
    }
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=gender_choice, null=True)
    DOB = models.DateField(null=True)
    email = models.EmailField(max_length=100, null=True)
    nationality = models.CharField(max_length=100, null=True)
    
    
    
    def __str__ (self):
        return self.user.first_name
    
    
    
    

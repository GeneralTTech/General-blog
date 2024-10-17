from django.contrib import admin
from .models import Account, ProfileImage, Bio, BackgroundImage, Advertisement



# Register your models here.
admin.site.register(Advertisement)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'has_profile',)
    list_display_links = ('id','has_profile')
    

@admin.register(ProfileImage)
class ProfileImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'profile_picture',)
   
@admin.register(BackgroundImage)
class BackgroundImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'background_image',)
 
    
    
@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)
    

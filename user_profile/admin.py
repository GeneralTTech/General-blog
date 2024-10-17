from django.contrib import admin
from .models import UserProfile

# Register your models here.
@admin.register(UserProfile)
class UserprofiletAdmin(admin.ModelAdmin):
    list_display = ('id', 'gender', 'DOB', 'email',)
    list_display_links = ('id',)
    search_fields = ('id', 'email',)
from django.contrib import admin
from .models import Post , Category, Comment



# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'Category', 'slug')
    prepopulated_fields = {'slug':('Category',)}



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'category', 'title', 'created',)
    list_display_links = ('id', 'user') 
    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)
    list_display_links = ('id', 'user') 
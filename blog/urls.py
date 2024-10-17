from django.urls import path
from . import views


urlpatterns = [
  path('',views.home,name='home_page'),   
  path('<slug:category_slug>/',views.home,name='post-by-category'),   
  path('create/post/',views.post,name='post_page'),  
  path('read/post/<str:pk>',views.read_post,name='read_post_page'),
  path('about/<str:username>/',views.about_user,name='about-user'),
  path('edit/<str:pk>/',views.edit_post,name='edit-post'),
  path('delete/<str:pk>/',views.delete_post,name='delete-post'),
  path('comment/<str:pk>/',views.comment,name='comment'),
]

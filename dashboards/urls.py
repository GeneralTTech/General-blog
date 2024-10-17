from django.urls import path
from . import views



urlpatterns = [
    path('', views.dashboard, name='user-dashboard'),
    path('<slug:user_slug>/', views.dashboard, name='user-about'),
    path('upload/profile', views.upload_profile, name='profile-upload'),
]

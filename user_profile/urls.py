from django.urls import path
from . import views

urlpatterns = [
    path('',views.about_,name='about'),
    path('update/profile/',views.update_profile,name='update_profile_page'),
]

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_profile, name='upload_profile'),
    path('profiles/', views.profile_list, name='profile_list'),


   

] 

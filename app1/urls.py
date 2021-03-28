"""Connect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.Home,name='home'),
    path('login/',views.Login,name='login'),
    path('register/',views.Register,name='register'),
    path('register/step1/<slug:userid>',views.Register_step1,name='register_step1'),
    path('dashboard/',views.Dashboard,name='dashboard'),
    path('userprofile/<slug:userid>',views.UserProfile,name='userProfile'),
    path('aboutus/',views.AboutUs,name='aboutus'),
    path('logout/', views.Logout, name='Logout')
]

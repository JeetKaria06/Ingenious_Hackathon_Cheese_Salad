from django.http.response import HttpResponse
from django.shortcuts import render
from .form_app1 import loginForm,registerForm,registerForm_1

# Create your views here.


def Home(request):
    return render(request,'index.html')



def Login(request):    
    loginform=loginForm()
    return render(request,'login.html',{'form':loginform})


def Register(request):
    register=registerForm()
    return render(request,'register.html',{'form':register})


def Register_step1(request,userid):
    register=registerForm_1()
    return render(request,'register_step1.html',{'form':register})

from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import admin

from django.contrib import messages
from django.utils.text import capfirst
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.
def home(request):
    return render(request,'home.html')
def admin(request):
    return render(request,'admin.html')


def add_video(request):
    if request.method == 'POST':
        if request.FILES.get('file') is not None:
            vid=  request.FILES.get('file')
        else:
            vid = ''
        video1(video =vid).save()
        return redirect('admin')

    return render(request,'video.html')

def add_contact(request):

    if request.method == 'POST':

        full_name=request.POST['fullname']
        email=request.POST['email']
        company = request.POST['comp']
        c_num = request.POST['cnum']
        mssg = request.POST['msg']
        
        ct = contact_det(name = full_name,email= email,company = company,phone= c_num,message = mssg)
        ct.save()
         
        return redirect('home')

    return render(request,'contact.html')

def login(request):
        
    if request.method == 'POST':
        
        username = request.POST['uname']
        password = request.POST['pswd']
        user = auth.authenticate(username= username,password=password)
        if user is not None:
          if user.is_staff:
                auth.login(request,user)
                return redirect('admin')
                      
        else:
            messages.info(request,"Invalid Username or Password")
            return redirect('/home')
    
    return redirect('home')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('home')
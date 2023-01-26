from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import admin

from django.contrib import messages
from django.utils.text import capfirst
from django.contrib.auth.decorators import login_required

from .models import *

def home(request):
    return render(request,'home.html')


def admin_home(request):
    return render(request,'admin.html')

@login_required(login_url='login')
def add_video(request):
    if request.method == 'POST':
        if request.FILES.get('file') is not None:
            vid=  request.FILES.get('file')
        else:
            vid = ''
        video1(video_file =vid).save()
        return redirect('admin_home')

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
         
        return redirect('add_contact')
        
    vid = video1.objects.all().last()
    context = {'video' : vid }
    return render(request,'contact.html', context)

@login_required(login_url='login')
def show_contact(request):
    cnt = contact_det.objects.all()
    context = {
        'contact' : cnt
    }
    return render(request, 'show_contact.html', context)

@login_required(login_url='login')
def edit_contact(request,pk):

    cnt = contact_det.objects.get(id = pk)
        
    if request.method == "POST":

      
        cnt.name = request.POST.get('fullname')
        cnt.email  = request.POST.get('email')
        cnt.company = request.POST.get('comp')
        cnt.phone = request.POST.get('cnum')
        cnt.message = request.POST.get('msg')
            

        cnt.save()
        
        return redirect('show_contact')

    context = {
        'contact' : cnt, 
    }
    return render(request,'edit_contact.html',context)

@login_required(login_url='login')
def del_contact(request,pk):
    cnt = contact_det.objects.get(id = pk)
    cnt.delete()
    return redirect('show_contact')

def login(request):
        
    if request.method == 'POST':
        
        username = request.POST['uname']
        password = request.POST['pswd']
        user = auth.authenticate(username= username,password=password)
        if user is not None:
          if user.is_staff:
                auth.login(request,user)
                return redirect('admin_home')
                      
        else:
            messages.info(request,"Invalid Username or Password")
            return redirect('home')
    
    return redirect('home')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('home')
from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from myapp.models import Querry
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login 

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        number=request.POST['snumber']
        email=request.POST['semail']
        password=request.POST['password']
        repeatpassword=request.POST['rpword']


        if len(number)<10:
            messages.error(request,'Number Should be 10 digits.')
            return redirect("/register") 
        elif password != repeatpassword:
            messages.error(request,"Passwords don't match")
            return redirect("/register") 
        else:
            my_user= User.objects.create_user(username=username,password=password, email=email)
            my_user.save()
            messages.success(request,'Account Created Successfully.') 
            return redirect("/login")
    return render(request, 'myapp/register.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=authenticate(request, username=username,password=password)
            print(user)

        except Exception as e:
            print(e)        
        if user is not None:
            auth_login(request,user)
            messages.success(request, "Logged in successfully..")
            return redirect("/")                     
        else:
          messages.error(request,"Something went wrong..") 
          return redirect("/login")    
    return render(request, 'myapp/login.html')


   

def home(request):
    return render(request, 'myapp/home.html')
    
def about(request):
    return render(request, 'myapp/about.html')
def dryFruits(request):
    return render(request, 'myapp/dryFruits.html')
def contact(request):
    return render(request, 'myapp/contact.html')
# def register(request):
#     return render(request, 'myapp/register.html')
   
def rice_and_pulses(request):
    return render(request, 'myapp/rice_and_pulses.html')

#contact form submission view    
def submitted(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        address=request.POST.get('address')
        zip_code=request.POST.get('zip_code')
        order_description=request.POST.get('order_description')
        #pehla wala hai model ka name equal k right side pe hai value jo ki get kri hai humne
        en=Querry(name=name,email=email,number=number,address=address,zip_code=zip_code,order_description=order_description)
        en.save()


    return render(request, 'myapp/contact.html')
# user_login view
 
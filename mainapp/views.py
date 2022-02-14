from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login,logout
from matplotlib.style import context

from mainapp.forms import UserCreate

from django.contrib.auth.models import User


from django.contrib.auth.models import Group 
from django import template

def Indexpage(request):
      return render(request,"mainapp/index.html")
 

def Loginer(request):
    
    if request.method=="POST":
        UserName=request.POST.get("username")
        UserPassword=request.POST.get("password")
        user=authenticate(request,username=UserName, password=UserPassword)
        if user is not None:
            login(request,user)
            
            return redirect("indexpage")
        else:
            return render(request,"mainapp/user/login.html",{"warring":"true"})
   
    return render(request,"mainapp/user/login.html")


def Logouter(request):
    logout(request)
    return redirect("indexpage")


#TODO:user will be added by query, for all fields !!!!!!!!!!!!!!!!!!!!!!!!!
def UserCreator(request):
    context=UserCreate()
    if request.POST:
        user=UserCreate(request.POST)
        if user.is_valid():
            password = request.POST.get('password')
            user = user.save(commit=False)
            user.set_password(password)
            user.is_active=False
            user.save()
            return redirect("congratulations")
    return render(request,'mainapp/user/usercreate.html',{"context":context})


def Congratulatory(request):
    

    return render(request,'mainapp/user/congratulations.html')


from django.contrib.auth import get_user_model


def Staff(request):
    if request.user.is_authenticated:
        Usr = get_user_model()
        context = Usr.objects.filter(is_active=False)
        if "username" in request.POST:
                 username=request.POST.get("username")
               
                 try:
                    user=Usr.objects.filter(username=username)
                    
                    warring=False
                    if len(user)==0:
                        warring=True
                    
                    return render(request,"mainapp/user/staff.html",{"context":None,"context2":user,"warring":warring})
                 except:
                    return render(request,"mainapp/user/staff.html",{"context":None,})



    else:
        context="bye.."

    return render(request,'mainapp/user/staff.html',{"context":context})


def Activator(request,id):
    if request.user.is_authenticated:
        user=User.objects.get(pk=id)
        user.is_active=True
        user.save()
        return redirect("staff")

def DeActivator(request,id):
    if request.user.is_authenticated:
        user=User.objects.get(pk=id)
        user.is_active=False
        user.save()
        return redirect("staff")
    




register = template.Library() 
def is_group(user, group_name):
    group =  Group.objects.get(name=group_name) 
    return group in user.groups.all() 

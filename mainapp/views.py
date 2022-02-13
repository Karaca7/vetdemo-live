from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login,logout

from mainapp.forms import UserCreate

from django.contrib.auth.models import User


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
            user.save()
            user=authenticate(request,username=user.username, password=password)
            if user is not None:
                login(request,user)

                return redirect("indexpage")
    return render(request,'mainapp/user/usercreate.html',{"context":context})




    
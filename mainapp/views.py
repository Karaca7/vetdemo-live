from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login,logout


def indexpage(request):
      return render(request,"mainapp/index.html")



 

def loginer(request):
    
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


def logouter(request):
    logout(request)
    return redirect("indexpage")
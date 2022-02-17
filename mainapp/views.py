
from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login,logout

from mainapp.forms import UserCreate

from django.contrib.auth.models import User



from django.contrib.auth import get_user_model


from django.views.generic import TemplateView,View



class IndexView(TemplateView):
    template_name="mainapp/index.html"


class LoginView(View):
    template_name="mainapp/user/login.html"
    
    def get(self,request):
        return render(request,self.template_name)

    def post(self,request):
        UserName=request.POST.get("username")
        UserPassword=request.POST.get("password")
        user=authenticate(request,username=UserName, password=UserPassword)
        if user is not None:
            login(request,user)
            
            return redirect("indexpage")
        else:
            return render(request,self.template_name,{"warring":"true"})



def Logouter(request):
    logout(request)
    return redirect("indexpage")


#TODO:user will be added by query, for all fields !!!!!!!!!!!!!!!!!!!!!!!!!

class UserCreateorView(View):
    template_name="mainapp/user/usercreate.html"
    form_class=UserCreate

    def get(self,request):
        return render(request,self.template_name,{"context":self.form_class})

    def post(self,request):
        user=self.form_class(request.POST)
        if user.is_valid():
            print("asdf")
            password = request.POST.get('password')
            user = user.save(commit=False)
            user.set_password(password)
            user.is_active=False
            user.save()
            return redirect("congratulations")
        return render(request,self.template_name,{"context":self.form_class})
 

        
class CongratulatoryVıew(TemplateView):
    template_name='mainapp/user/congratulations.html'



class StaffView(View):

    def get(self,request):
        if request.user.is_authenticated:

            Usr = get_user_model()
            context = Usr.objects.filter(is_active=False)
            return render(request,"mainapp/user/staff.html",{"context":context})
        else:
            return redirect("indexpage")

    def post(self,request):
        if request.user.is_authenticated:
            Usr = get_user_model()
            context = Usr.objects.filter(is_active=False)

            if "username" in request.POST:
                    username=request.POST.get("username")
                
                    try:
                        user=Usr.objects.filter(username=username)
                        warring=False
                        if not user:
                            print(123)
                            warring=True
                        
                        return render(request,"mainapp/user/staff.html",{"context":None,"context2":user,"warring":warring})
                    except:
                        return render(request,"mainapp/user/staff.html",{"context":None,})
        else:
            return redirect("indexpage")
        



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
    





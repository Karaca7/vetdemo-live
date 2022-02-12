from tokenize import Name
from django.shortcuts import redirect, render ,HttpResponse

from userpage.forms import PetForm,PetOwnerForm
from django.contrib.auth.models import User

from userpage.models import Pet,PetOwner
# Create your views here.



def Userp(request):
    if request.user.is_authenticated:
   
        context=Pet.objects.all()

        if request.method=="POST":
           
            if "petowenname" in request.POST:
                 ownername=request.POST.get("petowenname")
                 try:
                    owners=  Pet.objects.filter( PetO__Name__contains=ownername ) #PetOwner.objects.filter(Name=ownername)
                    warring=False
                    if len(owners)==0:
                        warring=True
                  
                    return render(request,"userpage/userpage.html",{"context":context,"context2":owners,"warring":warring})
                 except:
                    return render(request,"userpage/userpage.html",{"context":context,"warring":True})



            if "petname" in request.POST:
                 petname=request.POST.get("petname")
               
                 try:
                    pets=Pet.objects.filter(PetName=petname)
                    warring=False
                    if len(pets)==0:
                        warring=True
                    
                    return render(request,"userpage/userpage.html",{"context":context,"context2":pets,"warring":warring})
                 except:
                    return render(request,"userpage/userpage.html",{"context":context,})

    else:
         return redirect("indexpage")
    return render(request,"userpage/userpage.html",{"context":context})






def Addpet(request):
    form=PetForm()
    
    if(request.method=="POST"):
           form=PetForm(request.POST)
           pet = form.save(commit=False)     
         
           pet.Vet= request.user
           pet.save()
           return redirect("main") 
           
    return render(request,"userpage/addpet.html",{"FORM":form})
   
    
    
    



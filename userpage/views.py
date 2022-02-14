from queue import Empty
from tokenize import Name
from django.shortcuts import redirect, render ,HttpResponse
from sqlalchemy import null

from userpage.forms import PetForm,PetOwnerForm
from django.contrib.auth.models import User

from userpage.models import Pet,PetOwner


from django.core.paginator import Paginator,EmptyPage
# Create your views here.




def Userp(request):
    if request.user.is_authenticated:
   
       
        if request.method=="POST":
           
            if "petowenname" in request.POST:  # this will be  Get method !!!
                 ownername=request.POST.get("petowenname") 
                 try: 
                    owners=  Pet.objects.filter( PetO__Name__contains=ownername ) 
                    warring=False
                    if len(owners)==0:
                        warring=True


                    
                  
                    return render(request,"userpage/userpage.html",{"context":None,"context2":owners,"warring":warring})
                 except:
                    return render(request,"userpage/userpage.html",{"context":None,"warring":True})

            if "petname" in request.POST:
                 petname=request.POST.get("petname")
               
                 try:
                    pets=Pet.objects.filter(PetName=petname)
                    
                    warring=False
                    if len(pets)==0:
                        warring=True
                    
                    return render(request,"userpage/userpage.html",{"context":None,"context2":pets,"warring":warring})
                 except:
                    return render(request,"userpage/userpage.html",{"context":None,})
    else:
         return redirect("indexpage")
    
    if request.method=="GET":
        context=Pet.objects.all()
        p=Paginator(context,2)
        page_num=request.GET.get('page',1)
        try:
            page=p.page(page_num)
        except EmptyPage:
            page=p.page(1)
            
        context=page

        return render(request,"userpage/userpage.html",{"context":context})
    return render(request,"userpage/userpage.html")
   


def Addpet(request):

    if request.user.is_authenticated:
        form=PetForm()
        
        if(request.method=="POST"):
            form=PetForm(request.POST,request.FILES)
            if form.is_valid(): 
                pet = form.save(commit=False)     
                pet.Vet= request.user
                pet.save()
                return redirect("main") 
            else:
                print("......")
    else:
        form="bye..."
            
    return render(request,"userpage/addpet.html",{"FORM":form})
   
    
    


def AddPetOwner(request):

    if request.user.is_authenticated:
        form=PetOwnerForm()
        
        if(request.method=="POST"):
            form=PetOwnerForm(request.POST)
            owner=form.save(commit=False)
            owner.Vet=request.user
            owner.save()
            return redirect("main")
    else:
        form="bye..."    
           
    return render(request,"userpage/addpetowner.html",{"FORM":form})





def UpdatePet(request,id):

    if request.user.is_authenticated:

        pet=Pet.objects.get(pk=id)

        form=PetForm(instance=pet)
        if request.method=="POST":
            pet=Pet.objects.get(pk=id)
            pet.PetName=request.POST.get("PetName")
            pet.PetAge=request.POST.get("PetAge")
            pet.PetType=request.POST.get("PetType")
            changedPetowner=PetOwner.objects.get(pk=request.POST.get("PetO")) 
            pet.PetO=changedPetowner
            pet.save()
            return redirect("main")
    else:
        form="bye..."   
    return render(request,"userpage/updatepet.html",{"form":form})



#TODO: I WİLL NEW DATAMODELS CLİNT DATAS' CAN DELETE BUT WE  ADD ORTHER DATA MODELS İNTO !!!

def DeletePet(request,id):

    if request.user.is_authenticated:
        pet=Pet.objects.get(pk=id)
        pet.delete()
    return redirect("main")
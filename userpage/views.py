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

                 print(pets)

           
           

            # print(optionss)
            # try:
            #     #if bloğu ile selected koyup bir owner arama bir de pet arama ile ayrılacak

            #     # petowner=PetOwner.objects.filter(pet__PetName=value,Name=value2)#this isss join python magic spesific search
    
            #     if optionss=="owner":

            #         print(1)
            #         search=PetOwner.objects.filter(Name=value2)
            #     else:
            #         print(2)
            #         search=Pet.objects.filter(PetName=value)
            #         return render(request,"userpage/userpage.html",{"context":context,"context2":search})
            
            # except:
            #     return render(request,"userpage/userpage.html",{"context":context,"context2":"there is no such content"})

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
   
    
    


def AddPetOwner(request):
    form=PetOwnerForm()
    
    if(request.method=="POST"):
        form=PetOwnerForm(request.POST)
        owner=form.save(commit=False)
        owner.Vet=request.user
        owner.save()

        return redirect("main")  
         
         
           
    return render(request,"userpage/addpetowner.html",{"FORM":form})





def UpdatePet(request,id):

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


    return render(request,"userpage/updatepet.html",{"form":form})




def DeletePet(request,id):
#TODO: I WİLL NEW DATAMODELS CLİNT DATAS' CAN DELETE BUT WE  ADD ORTHER DATA MODELS İNTO !!!
    pet=Pet.objects.get(pk=id)
    pet.delete()
    return redirect("main")
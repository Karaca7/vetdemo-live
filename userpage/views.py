
from django.shortcuts import redirect, render 

from userpage.forms import PetForm,PetOwnerForm


from userpage.models import Pet,PetOwner


from django.core.paginator import Paginator,EmptyPage
# Create your views here.

from django.views.generic import View



class UserPageView(View):
   

    def get(self,request):
        if request.user.is_authenticated:
           
            context=Pet.objects.all()
            p=Paginator(context,2)
            page_num=request.GET.get('page',1)
            try:
                page=p.page(page_num)
            except EmptyPage:
                page=p.page(1)
                
            context=page

            return render(request,"userpage/userpage.html",{"context":context})
        else:
            return redirect("indexpage")

    def post(self,request):
        if request.user.is_authenticated:
                
            if "petowenname" in request.POST:  
                    ownername=request.POST.get("petowenname") 
                    try: 
                        owners=  Pet.objects.filter( PetO__Name__contains=ownername ) 

                        warring=False
                        if not owners:
                            warring=True
         
                        return render(request,"userpage/userpage.html",{"context":None,"context2":owners,"warring":warring})
                    except:
                        return render(request,"userpage/userpage.html",{"context":None,"warring":True})

            if "petname" in request.POST:
                    petname=request.POST.get("petname")
                
                    try:
                        pets=Pet.objects.filter(PetName=petname)
                        
                        warring=False
                        if not pets:
                            print("buraas")
                            warring=True
                        
                        return render(request,"userpage/userpage.html",{"context":None,"context2":pets,"warring":warring})
                    except:
                        return render(request,"userpage/userpage.html",{"context":None,})

            else:
                return redirect("indexpage")
                    



class AddPetView(View):
    template_name="userpage/addpet.html"
    form_class= PetForm

   
    def get(self,request):
        if request.user.is_authenticated:
            context={"FORM":self.form_class}
            return render(request,self.template_name,context)
        else:
            return redirect("indexpage")
        
    def post(self,request):

        if request.user.is_authenticated:
            form=self.form_class(request.POST,request.FILES)
            if form.is_valid(): 
                    pet = form.save(commit=False)     
                    pet.Vet= request.user
                    pet.save()
                    return redirect("main") 
           
        else:
            return redirect("indexpage")
        
       


class AddPetOwnerView(View):
    
    template_name="userpage/addpetowner.html"
    form_class=PetOwnerForm

    def get(self,request):
        if request.user.is_authenticated:
            return render(request,self.template_name,{"FORM":self.form_class})
        else:
            return redirect("indexpage")

    def post(self,request):
        if request.user.is_authenticated:
            form=self.form_class(request.POST)
            owner=form.save(commit=False)
            owner.Vet=request.user
            owner.save()
            return redirect("main")

        else:
            return redirect("indexpage")


class UpdatePetView(View):
    template_name="userpage/updatepet.html"

    def get(self,request,id):
        if request.user.is_authenticated:
            try:
                pet=Pet.objects.get(pk=id) # todo :will return warring get_object_or_404() --- ı will use
            except:
                return redirect("main")

            form=PetForm(instance=pet)
            pet=Pet.objects.get(pk=id)
            return render(request,"userpage/updatepet.html",{"form":form})
        else:
            return redirect("indexpage")

      
    def post(self,request,id):
        if request.user.is_authenticated:
            try:
                pet=Pet.objects.get(pk=id) # todo :will return warring get_object_or_404() --- ı will use
            except:
                return redirect("main")
            
            form=PetForm(instance=pet)
            pet=Pet.objects.get(pk=id)
            pet=Pet.objects.get(pk=id)
            pet.PetName=request.POST.get("PetName")
            pet.PetAge=request.POST.get("PetAge")
            pet.PetType=request.POST.get("PetType")
            changedPetowner=PetOwner.objects.get(pk=request.POST.get("PetO")) 
            pet.PetO=changedPetowner
            pet.save()
            return redirect("main")
        else:
            return redirect("indexpage")
        



#TODO: I WİLL NEW DATAMODELS CLİNT DATAS' CAN DELETE BUT WE  ADD ORTHER DATA MODELS İNTO !!!

def DeletePet(request,id):

    if request.user.is_authenticated:
        print("delete")

        
        try:

            pet=Pet.objects.get(pk=id)
            pet.delete()
        except:
            redirect("main") # todo : will return warring
        
    return redirect("main")




from django.forms import ModelForm
from userpage.models import Pet,PetOwner

from django import forms

class PetForm(ModelForm):
    class Meta:
        model=Pet
        fields=["PetName","PetAge","PetType","PetExplan","PetO"]
        
    



class PetOwnerForm(ModelForm):
    class Meta:
        model=PetOwner
        fields=["Name","Surname","Address","Phone","Email"]




 
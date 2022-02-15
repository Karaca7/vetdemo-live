

from django.forms import ModelForm
from userpage.models import Pet,PetOwner

from django import forms
from django.core.exceptions import ValidationError



class PetForm(ModelForm):
    class Meta:
        model=Pet
        fields=["PetName","PetAge","PetType","PetExplan","PetO","PetImage"]

    def clean(self):
         owner=self.cleaned_data.get('PetO')
         if Pet.objects.filter(PetO=owner).count()>20:
              raise ValidationError('Draft entries may not have a publication date.')
             
    

            
        
    



class PetOwnerForm(ModelForm):
    class Meta:
        model=PetOwner
        fields=["Name","Surname","Address","Phone","Email"]




 
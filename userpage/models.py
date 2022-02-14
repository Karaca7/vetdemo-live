from distutils.command.upload import upload
from django.db import models

# Create your models here.



from django.contrib.auth.models import User

class PetOwner(models.Model):
  
    Name=models.CharField(max_length=20)
    Surname=models.CharField(max_length=20)
    Address=models.TextField()
    Phone=models.CharField(max_length=11)
    Email=models.CharField(max_length=100)
    Vet=models.ForeignKey(User,default="",on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class Pet(models.Model):
    

    PetName=models.CharField(max_length=20)
    PetAge=models.CharField(max_length=3)
    PetImage=models.ImageField(upload_to="pets",null=True, blank=True)
    PetType=models.CharField(max_length=20)
    PetExplan=models.TextField()
    PetO=models.ForeignKey(PetOwner, default="",on_delete=models.CASCADE)
    Vet=models.ForeignKey(User,default="",on_delete=models.CASCADE)
    def __str__(self):
        return self.PetName

    # def save(self,id,*args,**kwargs,):
    #     owners=PetOwner.objects.get(pk=id)
    #     if Pet.objects.filter(PetO=owners).count()<=5:
    #         super(Pet,self).save(*args,**kwargs)
    #     else:
    #         return "YOU DONT NEW RECORD"
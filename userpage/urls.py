
from django.contrib import admin
from django.urls import path
from userpage import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path("",views.Userp,name="main"),
        path("addpet/",views.Addpet,name="addpet"),
        path("addpetowner/",views.AddPetOwner,name="addpetowner"),
        path("updatepet/<int:id>",views.UpdatePet,name="updatepet"),
        path("deletepet/<int:id>",views.DeletePet,name="deletepet"), 
    
]

    

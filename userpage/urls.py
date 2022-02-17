
from django.contrib import admin
from django.urls import path
from userpage import views
from django.conf import settings
from django.conf.urls.static import static

from userpage.views import AddPetView,AddPetOwnerView, UpdatePetView,UserPageView

urlpatterns = [
        path("",UserPageView.as_view(),name="main"),
        path("addpet/",AddPetView.as_view(),name="addpet"),
        path("addpetowner/",AddPetOwnerView.as_view(),name="addpetowner"),
        path("updatepet/<int:id>",UpdatePetView.as_view(),name="updatepet"),
        path("deletepet/<int:id>",views.DeletePet,name="deletepet"), 
]

    

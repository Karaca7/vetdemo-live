
from django.contrib import admin
from django.urls import path
from userpage import views


urlpatterns = [
        path("",views.Userp,name="main"),

    
]
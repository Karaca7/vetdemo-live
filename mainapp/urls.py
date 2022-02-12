from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.indexpage,name="indexpage"),
    path("user/",include("userpage.urls")),
    path("login/",views.loginer,name="llogin"),
    path("logout/",views.logouter,name="logout"),
]
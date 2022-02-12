from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.Indexpage,name="indexpage"),
    path("user/",include("userpage.urls")),
    path("login/",views.Loginer,name="llogin"),
    path("logout/",views.Logouter,name="logout"),
    path("usercreate",views.UserCreator,name="usercreate")

]
from django.contrib import admin
from django.urls import path,include
from . import views
from mainapp.views import IndexView,LoginView,UserCreateorView,CongratulatoryVıew,StaffView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",IndexView.as_view(),name="indexpage"),
    path("user/",include("userpage.urls")),
    path("login/",LoginView.as_view(),name="llogin"),
    path("logout/",views.Logouter,name="logout"),
    path("usercreate/",UserCreateorView.as_view(),name="usercreate"),
    path("congratulations/",CongratulatoryVıew.as_view(),name="congratulations"),
    path("staff/",StaffView.as_view(),name="staff"),
    path("activator/<int:id>",views.Activator,name="activator"),
    path("deactivator/<int:id>",views.DeActivator,name="deactivator"),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
    # path("userupadte",views.UserUpdateor,name="userupdate"),

]
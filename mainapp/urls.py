from django.contrib import admin
from django.urls import path,include
from . import views


from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.Indexpage,name="indexpage"),
    path("user/",include("userpage.urls")),
    path("login/",views.Loginer,name="llogin"),
    path("logout/",views.Logouter,name="logout"),
    path("usercreate",views.UserCreator,name="usercreate"),
    # path("userupadte",views.UserUpdateor,name="userupdate"),
    path('change-password/', auth_views.PasswordChangeView.as_view()),

]
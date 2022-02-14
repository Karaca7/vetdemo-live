from django.contrib import admin
from django.urls import path,include
from . import views


from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.Indexpage,name="indexpage"),
    path("user/",include("userpage.urls")),
    path("login/",views.Loginer,name="llogin"),
    path("logout/",views.Logouter,name="logout"),
    path("usercreate/",views.UserCreator,name="usercreate"),
    path("congratulations/",views.Congratulatory,name="congratulations"),
    path("staff/",views.Staff,name="staff"),
    path("activator/<int:id>",views.Activator,name="activator"),
    path("deactivator/<int:id>",views.DeActivator,name="deactivator"),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
    # path("userupadte",views.UserUpdateor,name="userupdate"),

]
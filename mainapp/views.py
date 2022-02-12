from django.shortcuts import render,HttpResponse




def indexpage(request):
    return HttpResponse("<h1>indexpage</h1>")

from django.shortcuts import render,HttpResponse




def indexpage(request):
      return render(request,"mainapp/index.html")

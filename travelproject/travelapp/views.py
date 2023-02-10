from django.http import  HttpResponse
from django.shortcuts import render
from .models import place
from .models import name
# Create your views here.
def demo(request):
    obj=place.objects.all()
    avj=name.objects.all()
    return render(request,"index.html",{'result':obj},{'solution':avj})
# def addition(request):
#     x=request.GET['num1']
#     y=request.GET['num2']
#     res=x+y
#
#     return render(request,"about.html",{"result":res})
# # def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return HttpResponse("hello am contact")
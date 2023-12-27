from django.shortcuts import render,HttpResponse
from app1.models import *

# Create your views here.

def topic(request):
     if request.method=='POST':
          to=request.POST['to']
          NTO=Topic.objects.get_or_create(topic_name=to)[0]
          NTO.save()
          return HttpResponse('Topic is inserted')

     return render(request,'topic.html')



def webpage(request):
     if request.method=='POST':
          
          to=request.POST['to']
          TO=Topic.objects.get(topic_name=to)
          n=request.POST['wp']
          u=request.POST['u']
          NWO=WebPage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
          NWO.save()
          return HttpResponse('webpage is created')
     return render(request,'webpage.html')
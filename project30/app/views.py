from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('Topic inserted')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WFO=WebpageForm()
    d={'WFO':WFO}

    if request.method=='POST':
        WPFO=TopicForm(request.POST)
        if WPFO.is_valid():
            WPFO.save()
            return HttpResponse('Webpage inserted')
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    AFO=AccessForm()
    d={'AFO':AFO}

    if request.method=='POST':
        APFO=TopicForm(request.POST)
        if APFO.is_valid():
            APFO.save()
            return HttpResponse('AccessRecord inserted')
    return render(request,'insert_access.html',d)

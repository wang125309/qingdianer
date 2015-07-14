# coding:utf8
from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect
import json
from django.conf import settings
from django.core.cache import cache
import random
import logging
from models import *
import datetime
import os

# Create your views here.

logger = logging.getLogger(__name__)

def index(request):
    p = products.objects.all()
    res = []
    for i in p:
        a = {}
        a['id'] = i.id
        a['title'] = i.title
        a['desc'] = i.desc
        a['URL'] = i.URL
        a['file'] =  i.file
        res.append(a)
    return render(request,"index.html",{
        "list" : res
    })


def delPro(request):
    p = products.objects.get(id=request.GET['id'])
    p.delete()
    return JsonResponse({
        "error_no":"0"
    }) 

def add(request):
    title = request.POST.get('title')
    desc = request.POST.get('desc')
    URL = request.POST.get('URL')
    file = request.POST.get('file')
    f = request.FILES.getlist('file')
    p = products.objects.all()
    pcnt = len(p)
    print f[0]
    d = open('./data/image/'+str(pcnt+1)+'.'+str(f[0]).split('.')[-1],'wb+')

    for i in f[0]:
        d.write(i)
    d.close()
    np = products(title=title,desc=desc,URL=URL,file='/data/image/'+str(pcnt+1)+'.'+str(f[0]).split('.')[-1])
    np.save()
    return HttpResponseRedirect('/backend/index/')

def portal(request):
    p = products.objects.all()
    res = []
    for i in p :
        a = {}
        a['id'] = i.id
        a['title'] = i.title
        a['desc'] = i.desc
        a['URL'] = i.URL
        a['file'] =  i.file
        res.append(a)
    return render(request,"portal.html",{
        "list" : res
    })

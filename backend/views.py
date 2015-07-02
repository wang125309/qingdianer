# coding:utf8
from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect
import json
import requests
from django.conf import settings
from django.core.cache import cache
import random
import logging
from models import *
import datetime

# Create your views here.

logger = logging.getLogger(__name__)


def loginNeed(func):
    def _loginNeed(request):
        if not request.session.get("username",False):
            return HttpResponseRedirect("/backend/login/")
        else:
            return func(request)
    return _loginNeed

def login(request):
    return JsonResponse({
       "dsf":"dsfd"
    })

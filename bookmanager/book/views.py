from django.shortcuts import render

# Create your views here.

"""
    视图就是一个python函数
"""

from django.http import HttpRequest
from django.http import HttpResponse

# 期望用户输入index来访问视图函数


def index(request):

    return HttpResponse('OK')



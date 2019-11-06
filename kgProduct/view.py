# -*- coding: utf-8 -*-

"""
@Project  : kgProduct
@File     : view.py
@Author   : Call偶围城
@Date     : 2019/11/5
@Time     : 23:15
@Software : PyCharm
"""

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def charts(request):
    return render(request, 'charts.html')


def tables(request):
    return render(request, 'tables.html')


def forms(request):
    return render(request, 'forms.html')


def pages(request):
    return render(request, 'pages.html')


def login(request):
    return render(request, 'login.html')

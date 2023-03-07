from django.http import HttpResponse
from django.shortcuts import render


def index1(request):
    return HttpResponse("python")


def index2(request):
    return HttpResponse("html")
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the vukker index.")

def lala(request):
    return HttpResponse("Hello, world. You're at the vukker lala.")
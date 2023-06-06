from django.shortcuts import render
from django.http import HttpResponse #clase que permite ejecutar una respuesta http.
# Create your views here.

def index(request):
    return HttpResponse('Hello, world!')
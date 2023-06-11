from django.shortcuts import render
from django.http import HttpResponse #clase que permite ejecutar una respuesta http.
# Create your views here.


def index(request): #function base view
    return HttpResponse('Estas en la página principal de Premios Platzi app')


def detail(request,question_id):
    return HttpResponse(f"Estas viendo el detalle de  la pregunta número: {question_id}")

def results(request,question_id):
    return HttpResponse (f"Estas viendo los resultados de la pregunta número: {question_id}")

def vote(request,question_id):
    return  HttpResponse(f"Estas votando a la pregunta numero: {question_id}")




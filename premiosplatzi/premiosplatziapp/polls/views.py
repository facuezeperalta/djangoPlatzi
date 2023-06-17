from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect #clase que permite ejecutar una respuesta http.
# Create your views here.
from .models import Question, Choice
from django.urls import reverse

""" def index(request): #function base view
    latest_question_list = Question.objects.all()
    return render(request,"polls/index.html",{
        'latest_question_list' : latest_question_list
    })
    


def detail(request,question_id):
    question = get_object_or_404(Question,pk= question_id)
    return render(request,"polls/detail.html",{'question':question})


def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{
        "question": question,
    }) """
#creamos las vistas con clases de python.





def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request,"polls/detail.html", {
            "question": question,
            'error_message': 'No elegiste una respuesta'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args = (question.id,)))







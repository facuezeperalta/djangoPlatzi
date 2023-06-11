from django.urls import path


from . import views

app_name = "polls"
urlpatterns = [
    #ex: /poll/
    path('',views.index, name ='index'),
    #ex: /polls/5/ con esto acceso al detalle de la pregunta 5
    path('<int:question_id>/',views.detail, name='detail'),
    #ex: /polls/5/result con esto acceso a los resultados de la pregunta 5
    path('<int:question_id>/results',views.results, name='results'),
    #ex: /polls/5/vote con esto acceso a los votos de la de la pregunta 5
    path('<int:question_id>/vote',views.vote, name='vote'),
]

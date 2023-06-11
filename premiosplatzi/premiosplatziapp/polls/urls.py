from django.urls import path


from . import views


urlpatterns = [
    #ex: /poll/
    path('',views.index, name ='index'),
    #ex: /polls/5/ con esto acceso al detalle de la pregunta 5
    path('<int:question_id>/',views.detail, name='Vista 01'),
    #ex: /polls/5/result con esto acceso a los resultados de la pregunta 5
    path('<int:question_id>/results',views.results, name='Vista 02'),
    #ex: /polls/5/vote con esto acceso a los votos de la de la pregunta 5
    path('<int:question_id>/vote',views.vote, name='Vista 03'),
    #ex: /polls/5/detail
    path('<int:question_id>/detail',views.detail,name='vista 04')
]

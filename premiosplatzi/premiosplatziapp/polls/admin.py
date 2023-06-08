from django.contrib import admin
from .models import Question, Choice #linea de codigo que importa el model de Question

# Register your models here.

admin.site.register([Question,Choice]) #importo Question en el admin de polls

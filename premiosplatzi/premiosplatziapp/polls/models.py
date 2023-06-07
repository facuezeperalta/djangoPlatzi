import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    #id no se define, ya que crea el id o PK de manera automática.
    #con esto creamos la tabla de datos en programacion orientada a objetos
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text #retorno al question text como cadena de strings.
    
    def was_publish_recentyl(self): #retorna verdadero o falso si la pregunta fue publicada recientemente 
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) #timedelta es un obj que define una diferencia de tiempos.
    
    
    
    
        

class Choice(models.Model): 
    #el id no se define.
    question = models.ForeignKey(Question, on_delete= models.CASCADE) # on_delete= models.CASCADE: cada vez que borremos una pregunta lo demas se borra en cascada. asi no queda nada suelto.
    choice_text = models.CharField(max_length=250)
    votes = models.IntegerField(default=0) #default hace que el contador inicie en 0.

    def __str__(self):
        return self.choice_text
    




    




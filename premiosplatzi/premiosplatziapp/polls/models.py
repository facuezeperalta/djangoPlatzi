from django.db import models
# Create your models here.

class Question(models.Model):
    #id no se define, ya que crea el id o PK de manera automática.
    #con esto creamos la tabla de datos en programacion orientada a objetos
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model): 
    #el id no se define.
    question = models.ForeignKey(Question, on_delete= models.CASCADE) # on_delete= models.CASCADE: cada vez que borremos una pregunta lo demas se borra en cascada. asi no queda nada suelto.
    choice_text = models.CharField(max_length=250)
    votes = models.IntegerField(default=0) #default hace que el contador inicie en 0.




    




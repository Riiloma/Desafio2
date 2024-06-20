from django.db import models

# Create your models here.
class Tarea (models.Model):
    # id= models.AutoField(primary_key=True ,null=False)
    descripcion= models.TextField( max_length=400,default="")
    eliminada= models.BooleanField(default=False)

class SubTarea(models.Model):
    id= models.AutoField(primary_key=True ,null=False)
    descripcion= models.TextField(default="", max_length=400)
    eliminada= models.BooleanField(default=False)
    tarea= models.ForeignKey(Tarea, on_delete=models.CASCADE,)
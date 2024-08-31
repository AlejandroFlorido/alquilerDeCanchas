from django.db import models

# Create your models here.

class Cancha(models.Model):

    Nombre_cancha = models.CharField(max_length=50)
    id_cancha = models.CharField(primary_key=True, max_length=6)
    tipo = models.CharField(max_length=50)
    disponible = models.BooleanField()
    con_luz = models.BooleanField()
    horario_reservado = models.BooleanField()
    duracion_reserva = models.IntegerField()

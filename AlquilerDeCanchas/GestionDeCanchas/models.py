from django.db import models

# Create your models here.

class Cancha(models.Model):

    Nombre_cancha = models.CharField(max_length=50)
    id_cancha = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50)
    disponible = models.BooleanField()
    con_luz = models.BooleanField()
    horario_reservado = models.BooleanField()
    duracion_reserva = models.IntegerField()

    def __str__(self):

        texto = "{0} ({1})"
        
        return texto.format(self.Nombre_cancha, self.disponible)
    
class Cliente(models.Model):

    Nombre_completo = models.CharField(max_length=50)
    dni = models.BigIntegerField(primary_key=True)
    telefono = models.BigIntegerField()
    email = models.CharField(max_length=50)

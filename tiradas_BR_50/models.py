

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Tirada(models.Model):
    TIPO_TIRADA = [('Entrenamiento', 'Entrenamiento'), ('Campeonato', 'Campeonato')]
    MODALIDADES = [
        ('Aire: Varmint Ligero', 'Aire: Varmint Ligero'),
        ('Aire: Varmint Pesado', 'Aire: Varmint Pesado'),
        ('BR-50: Sporter', 'BR-50: Sporter'),
        ('BR-50: Varmint Ligero', 'BR-50: Varmint Ligero'),
        ('BR-50: Varmint Pesado', 'BR-50: Varmint Pesado'),
    ]
    DIRECCIONES_VIENTO = [
        ('N', 'Norte'),
        ('NO', 'Noroeste'),
        ('O', 'Oeste'),
        ('SO', 'Suroeste'),
        ('S', 'Sur'),
        ('SE', 'Sureste'),
        ('E', 'Este'),
        ('NE', 'Noreste'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tirador = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_TIRADA)
    campo = models.CharField(max_length=100)
    modalidad = models.CharField(max_length=30, choices=MODALIDADES)
    arma = models.CharField(max_length=100)
    marca_municion = models.CharField(max_length=100)
    numero_disparos = models.PositiveIntegerField()
    #puntuacion = models.DecimalField(max_digits=6, decimal_places=2)
    puntuacion = models.PositiveIntegerField()
    numero_dieces = models.PositiveIntegerField()
    direccion_viento = models.CharField(max_length=2, choices=DIRECCIONES_VIENTO)
    velocidad_viento = models.PositiveIntegerField()
    fecha = models.DateField()

    def __str__(self):
        return f'{self.tirador} - {self.tipo}'

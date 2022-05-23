from django.db import models
from localflavor.es.forms import ESIdentityCardNumberField

from django.contrib.auth.models import User
from .validaciones import *
import uuid

class Perfil(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(validators=[fecha_nacimiento_validacion])
    dni = ESIdentityCardNumberField(only_nif=True)
    posee_carnet_b = models.BooleanField()
    telefono = models.models.CharField(max_length=9)
    api_key = models.CharField(max_length=255, null=True, blank=True, unique=True, default=uuid.uuid4)
   
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
        
    def __str__(self):
        return self.usuario.username
            

class Vehiculo(models.Model): 
    
    MARCAS =  [
    ('AUDI', 'Audi'),
    ('BMW', 'Bmw'),
    ('OPEL', 'Opel'),
    ('MERCEDES', 'Mercedes'),
    ('TESLA', 'Tesla'),
    ]
    
    PUERTAS =  [
    ('3', '3'),
    ('4', '4'),
    ('5', '5'), 
    ]

    COMBUSTIBLES = [
    ('GASOIL', 'Gasoil'),
    ('GASOLINA', 'Gasolina'),
    ('ELECTRICO', 'Electrico'),
    ]
    
    TRANSMISION =   [
    ('AUTOMATICO', 'Automatico'),
    ('MANUAL', 'Manual'),
    ]
    foto = models.ImageField(blank=True,null=True) 
    marca = models.CharField(choices=MARCAS, max_length=15)
    modelo = models.CharField(max_length=255)
    matricula = models.CharField(max_length=7)
    cilindrada = models.IntegerField()
    asientos = models.IntegerField()
    puertas = models.CharField(choices=PUERTAS,max_length=1)
    combustible = models.CharField(choices=COMBUSTIBLES,max_length=9)
    precio_dia = models.FloatField()
    consumo =  models.FloatField()
    transmision = models.CharField(choices=TRANSMISION,max_length=10)

    class Meta:
        verbose_name = "Vehiculo"
        verbose_name_plural = "Vehiculos"
        
    def __str__(self):
        return self.marca + " " + self.modelo + " matricula: " + self.matricula

class Reservas(models.Model):
    vehiculo = models.ForeignKey(Vehiculo,on_delete=models.CASCADE)
    cliente = models.OneToOneField(User,on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    coste = models.FloatField()
        
    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        
    def __str__(self):
            return self.vehiculo + " " + self.cliente 
from django.db import models

# Create your models here.

class Luffy(models.Model):
    OPCIONES_HAKI = [
        ("armadura", "Haki de armadura"),
        ("observacion", "Haki de observacion"),
        ("rey", "Haki del rey")
    ]
    idLuffy = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=25)
    haki = models.CharField(max_length=25, choices=OPCIONES_HAKI)
    edad = models.IntegerField()
    dia = models.CharField(max_length=15)
    hora = models.CharField(max_length=10)
    

class Shanks(models.Model):
    OPCIONES_HAKI = [
        ("armadura", "Haki de armadura"),
        ("observacion", "Haki de observacion"),
        ("rey", "Haki del rey")
    ]
    idShanks = models.IntegerField(primary_key=True)
    haki = models.CharField(max_length=25, choices=OPCIONES_HAKI)
    nombre = models.CharField(max_length=25)
    edad = models.IntegerField()
    dia = models.CharField(max_length=15)
    hora = models.CharField(max_length=10)
    

class Teach(models.Model):
    OPCIONES_HAKI = [
        ("armadura", "Haki de armadura"),
        ("observacion", "Haki de observacion"),
        ("rey", "Haki del rey")
    ]
    idTeach = models.IntegerField(primary_key=True)
    haki = models.CharField(max_length=25, choices=OPCIONES_HAKI)
    nombre = models.CharField(max_length=25)
    edad = models.IntegerField()
    dia = models.CharField(max_length=15)
    hora = models.CharField(max_length=10)
    

class Buggy(models.Model):
    OPCIONES_HAKI = [
        ("armadura", "Haki de armadura"),
        ("observacion", "Haki de observacion"),
        ("rey", "Haki del rey")
    ]
    idBuggy = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=25)
    haki = models.CharField(max_length=25, choices=OPCIONES_HAKI)
    edad = models.IntegerField()
    dia = models.CharField(max_length=15)
    hora = models.CharField(max_length=10)
    
    

from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50)
    grado = models.CharField(max_length=50)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    
class ResumenDeCuenta(models.Model):
    estado = models.CharField(max_length=50)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    saldoPendiente = models.DecimalField(max_digits=10, decimal_places=2)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=True)
    fechaUltimaPago = models.DateField()
    
class ReciboDePago(models.Model):
    idRecibo = models.AutoField(primary_key=True)
    fechaPago = models.DateField()
    valorCancelado = models.DecimalField(max_digits=10, decimal_places=2)
    tipoDePago = models.CharField(max_length=50)
    ccDelResponsable = models.IntegerField()
    entidadBancaria = models.CharField(max_length=100)
    resumenDeCuenta = models.ForeignKey(ResumenDeCuenta, on_delete=models.CASCADE)
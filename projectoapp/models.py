from django.db import models

# Create your models here.
class Alumno(models.Model):
    rut = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length=50)
    fechacreacion = models.DateField()
    estado = models.IntegerField()
    
class Profesor(models.Model):
    rut = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length=50)
    fechacreacion = models.DateField()
    estado = models.IntegerField()    
    
class Asignatura(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.TextField(max_length=50)
    fechacreacion = models.DateField()
    estado = models.IntegerField() 

class Asistencia(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.TextField(max_length=50)
    fechacreacion = models.DateField()
    estado = models.IntegerField()   
    
class Plataforma(models.Model):
    idplataforma = models.IntegerField(primary_key=True)
    descripcion = models.TextField(max_length=50)
    fechacreacion = models.DateField()
    estado = models.IntegerField()  
    
class FormaPago(models.Model):
    idformapago = models.IntegerField(primary_key=True)
    descripcion = models.TextField(max_length=50)
    fechacreacion = models.DateField()
    estado = models.IntegerField()   
    
class Agenda(models.Model):
    id = models.IntegerField(primary_key=True)
    fechahorainicio = models.DateTimeField()           
    fechahorafin = models.DateTimeField()
    idasignatura = models.ForeignKey(Asignatura, on_delete=models.PROTECT)
    idprofesor = models.ForeignKey(Profesor, on_delete=models.PROTECT)
    estado = models.IntegerField()
    idagenda = models.ForeignKey('Agenda', on_delete=models.PROTECT)
    link = models.URLField()
    idplataforma = models.ForeignKey(Plataforma, on_delete=models.PROTECT)
    
class Pagos(models.Model):
    id = models.IntegerField(primary_key=True)
    idagenda = models.ForeignKey(Agenda, on_delete=models.PROTECT)
    fechapago = models.DateField()
    idformapago = models.ForeignKey(FormaPago, on_delete=models.PROTECT)
    rutalumno = models.ForeignKey(Alumno, on_delete=models.PROTECT)
    valor = models.IntegerField()
    estado = models.IntegerField()
    comision = models.IntegerField()    
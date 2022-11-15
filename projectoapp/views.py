import re
from urllib import request
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from projectoapp.models import *
from projectoapp.serializers import AgendaSrlz, AlumnoSrlz, AsignaturaSrlz, AsistenciaSrlz, FormaPagoSrlz, PagosSrlz, PlataformaSrlz, ProfesorSrlz
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSrlz

@csrf_exempt
def alumnos(request):
    if request.method == 'GET':
        alumnos = Alumno.objects.all()
        serializer = AlumnoSrlz(alumnos, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        print('recibiendo peticion POST')
        serializer = AlumnoSrlz(data=request.POST)
        if serializer.is_valid():
            print('peticion valida')
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serialazer_class = ProfesorSrlz
    
class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    serialazer_class = AsignaturaSrlz
        
class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serialazer_class = AsistenciaSrlz

class PlataformaViewSet(viewsets.ModelViewSet):
    queryset = Plataforma.objects.all()
    serialazer_class = PlataformaSrlz

class FormaPagoViewSet(viewsets.ModelViewSet):
    queryset = FormaPago.objects.all()
    serialazer_class = FormaPagoSrlz

class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serialazer_class = AgendaSrlz

class PagosViewSet(viewsets.ModelViewSet):
    queryset = Pagos.objects.all()
    serialazer_class = PagosSrlz                
            
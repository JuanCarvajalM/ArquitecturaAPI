from dataclasses import field
from urllib import response
from rest_framework import serializers
from projectoapp.models import *

class AlumnoSrlz(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class ProfesorSrlz(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'

class AsignaturaSrlz(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'

class AsistenciaSrlz(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'

class PlataformaSrlz(serializers.ModelSerializer):
    class Meta:
        model = Plataforma
        fields = '__all__'

class FormaPagoSrlz(serializers.ModelSerializer):
    class Meta:
        model = FormaPago
        fields = '__all__'

class AgendaSrlz(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = '__all__'

class PagosSrlz(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = '__all__'
        
from django import forms
from AduanaNacional.models import *

class ObjetoForm(forms.Form):
	origen = forms.CharField(max_length=100)
	fecha = forms.DateField()
	descripcion = forms.CharField(max_length=200)
	propietario = forms.CharField(max_length=50)
	foto = forms.ImageField()
	class Meta:
		model = Objeto
		fields = ('origen','fecha','descripcion','propietario','foto','zona')
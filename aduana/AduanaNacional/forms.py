from django.forms import ModelForm
from AduanaNacional.models import *

class ObjetoForm(ModelForm):
	class Meta:
		model = Objeto
		fields = ('origen','fecha','descripcion','propietario','foto')
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from AduanaNacional.forms import *
from AduanaNacional.models import *

from rest_framework import generics
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Persona
from .serializers import PersonaSerializer


def login(request):
	return render(request,'AduanaNacional/login.html')

def zonas(request):
	lista_zonas = Zona.objects.all()
	return render(request,'AduanaNacional/zonas.html',{"Zonas":lista_zonas})

def mapa(request):
	return render(request,'AduanaNacional/mapa.html')

def inventario(request,zona):
	lista_objetos = Objeto.objects.filter(zona=zona)
	return render(request,'AduanaNacional/inventario.html',{"Objetos":lista_objetos,"Zona":zona})

def objeto(request,zona,desc):
	objeto = Objeto.objects.get(descripcion=desc)
	return render(request,'AduanaNacional/objeto.html',{"Objeto":objeto})

def anadirObjeto(request,zona):
	if request.method=="POST":
		form = ObjetoForm(request.POST, request.FILES)
		if form.is_valid():
			origen = form.cleaned_data['origen']
			fecha = form.cleaned_data['fecha']
			descripcion = form.cleaned_data['descripcion']
			propietario = form.cleaned_data['propietario']
			foto = form.cleaned_data['foto']
			objeto = Objeto(origen=origen,fecha=fecha,descripcion=descripcion,propietario=propietario,foto=foto,zona=zona)
			objeto.save()
			return redirect('/AduanaNacional/inventario/'+zona+'/')
	else:
		form = ObjetoForm()
	return render(request,'AduanaNacional/anadirObjeto.html',{'form':form,'accion':"Añadir"})

def editar(request,zona,desc):
	objeto1 = Objeto.objects.get(descripcion=desc,zona=zona)
	form = ObjetoForm(instance=objeto1)
	if request.method=="POST":
		form = ObjetoForm(request.POST, request.FILES,instance=objeto1)
		if form.is_valid():
			origen = form.cleaned_data['origen']
			fecha = form.cleaned_data['fecha']
			descripcion = form.cleaned_data['descripcion']
			propietario = form.cleaned_data['propietario']
			foto = form.cleaned_data['foto']
			objeto = Objeto(origen=origen,fecha=fecha,descripcion=descripcion,propietario=propietario,foto=foto,zona=zona)
			objeto.save()
			objeto1.delete()
			return render(request,'AduanaNacional/objeto.html',{"Objeto":objeto})
	return render(request,'AduanaNacional/anadirObjeto.html',{'form':form,'accion':"Editar"})

def eliminar(request,zona,desc):
	objeto = Objeto.objects.get(descripcion=desc,zona=zona)
	objeto.delete()
	return inventario(request,zona)



class PersonaList(generics.ListCreateAPIView):
	queryset = Persona.objects.all()
	serializer_class = PersonaSerializer
	permission_classes = (IsAuthenticated,)
	authentication_class = (TokenAuthentication,)

def login2(request,form):
	return render(request,'logina.html')


class Logina(FormView):
    template_name = "logina.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('AduanaNacional:persona_list')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Logina,self).dispatch(request,*args,*kwargs)

    def form_valid(self,form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user = user)
        if token:
            login2(self.request, form.get_user())
            return super(Logina,self).form_valid(form)
	

from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from AduanaNacional.forms import *
from AduanaNacional.models import *

def login(request):
	return render(request,'AduanaNacional/login.html')

def zonas(request):
	lista_zonas = Zona.objects.all()
	return render(request,'AduanaNacional/zonas.html',{"Zonas":lista_zonas})

def mapa(request):
	return render(request,'AduanaNacional/mapa.html')

def inventario(request):
	return render(request,'AduanaNacional/inventario.html')

def objeto(request):
	return render(request,'AduanaNacional/objeto.html')

def anadirObjeto(request):
	if request.method=="POST":
		form = ObjetoForm(request.POST, request.FILES)
		if form.is_valid():
			origen = form.cleaned_data['origen']
			fecha = form.cleaned_data['fecha']
			descripcion = form.cleaned_data['descripcion']
			propietario = form.cleaned_data['propietario']
			foto = form.cleaned_data['foto']
			objeto = Objeto(origen=origen,fecha=fecha,descripcion=descripcion,propietario=propietario,foto=foto,zona="Zona 1")
			objeto.save()
			return redirect('/AduanaNacional/inventario.html/')
	else:
		form = ObjetoForm()
	return render(request,'AduanaNacional/anadirObjeto.html',{'form':form})
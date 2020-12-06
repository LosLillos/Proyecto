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
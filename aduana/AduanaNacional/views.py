from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

def login(request):
	return render(request,'AduanaNacional/login.html')

def zonas(request):
	return render(request,'AduanaNacional/zonas.html')

def mapa(request):
	return render(request,'AduanaNacional/mapa.html')

def inventario(request):
	return render(request,'AduanaNacional/inventario.html')

def objeto(request):
	return render(request,'AduanaNacional/objeto.html')

def anadirObjeto(request):
	return render(request,'AduanaNacional/anadirObjeto.html')
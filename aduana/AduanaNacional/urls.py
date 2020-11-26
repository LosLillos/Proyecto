from django.urls import path
from . import views

urlpatterns = [
	path('',views.login),
	path('AduanaNacional/login.html',views.login),
	path('AduanaNacional/zonas.html',views.zonas),
	path('AduanaNacional/mapa.html',views.mapa),
	path('AduanaNacional/inventario.html',views.inventario),
]
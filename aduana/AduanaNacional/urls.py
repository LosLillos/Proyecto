from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

urlpatterns = [
	path('',LoginView.as_view(template_name='AduanaNacional/login.html'),name="login"),
	path('logout',logout,name="logout"),
	path('AduanaNacional/login.html',LoginView.as_view(template_name='AduanaNacional/login.html'),name="login"),
	path('AduanaNacional/zonas.html',views.zonas),
	path('AduanaNacional/mapa.html',views.mapa),
	path('AduanaNacional/inventario.html',views.inventario),
	path('AduanaNacional/inventario/<str:zona>/',views.inventario2),
	path('AduanaNacional/objeto.html',views.objeto),
	path('AduanaNacional/anadirObjeto.html',views.anadirObjeto,name="anadirObjeto"),
]
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .views import PersonaList

urlpatterns = [
	path('',LoginView.as_view(template_name='AduanaNacional/login.html'),name="login"),
	path('logout',logout,name="logout"),
	path('AduanaNacional/login.html',LoginView.as_view(template_name='AduanaNacional/login.html'),name="login"),
	path('AduanaNacional/zonas.html',login_required(views.zonas)),
	path('AduanaNacional/mapa.html',views.mapa),
	path('AduanaNacional/inventario/<str:zona>/',login_required(views.inventario)),
	path('AduanaNacional/inventario/<str:zona>/<str:desc>/',login_required(views.objeto)),
	path('AduanaNacional/anadirObjeto/<str:zona>/',login_required(views.anadirObjeto),name="anadirObjeto"),
	path('AduanaNacional/eliminar/<str:zona>/<str:desc>/',login_required(views.eliminar)),
	path('AduanaNacional/editar/<str:zona>/<str:desc>/',login_required(views.editar)),
	path('AduanaNacional/inventarioFiltrar/<str:zona>/',login_required(views.filtrar)),

	path('persona/',PersonaList.as_view(), name = 'persona_list'),
]
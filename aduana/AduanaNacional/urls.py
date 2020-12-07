from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

from .views import PersonaList

urlpatterns = [
	path('',LoginView.as_view(template_name='AduanaNacional/login.html'),name="login"),
	path('logout',logout,name="logout"),
	path('AduanaNacional/login.html',LoginView.as_view(template_name='AduanaNacional/login.html'),name="login"),
	path('AduanaNacional/zonas.html',views.zonas),
	path('AduanaNacional/mapa.html',views.mapa),
	path('AduanaNacional/inventario/<str:zona>/',views.inventario),
	path('AduanaNacional/inventario/<str:zona>/<str:desc>/',views.objeto),
	path('AduanaNacional/anadirObjeto/<str:zona>/',views.anadirObjeto,name="anadirObjeto"),
	path('AduanaNacional/eliminar/<str:zona>/<str:desc>/',views.eliminar),
	path('AduanaNacional/editar/<str:zona>/<str:desc>/',views.editar),
	path('AduanaNacional/inventarioFiltrar/<str:zona>/',views.filtrar),

	path('persona/',PersonaList.as_view(), name = 'persona_list'),
]
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
	path('',LoginView.as_view(template_name='AduanaNacional/login.html'),name="login"),
	path('AduanaNacional/login.html',LoginView.as_view(template_name='AduanaNacional/login.html'),name="login"),
	path('AduanaNacional/zonas.html',views.zonas),
	path('AduanaNacional/mapa.html',views.mapa),
	path('AduanaNacional/inventario.html',views.inventario),
]
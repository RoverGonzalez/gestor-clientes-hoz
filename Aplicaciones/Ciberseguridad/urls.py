from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarCliente/', views.registrarCliente),
    path('edicionCliente/<cuit>', views.edicionCliente),
    path('eliminarCliente/<cuit>', views.eliminarCliente),
    path('editarCliente/', views.editarCliente)
]
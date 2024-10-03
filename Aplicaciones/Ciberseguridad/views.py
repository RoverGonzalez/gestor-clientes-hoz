from django.shortcuts import render, redirect
from .models import Cliente
from django.contrib import messages

# Create your views here.

def home(request):
    clientes = Cliente.objects.all()
    return render(request, "gestionClientes.html", {"clientes": clientes})

def registrarCliente(request):
    cuit = request.POST['numCuit']
    empresa = request.POST['txtEmpresa']
    empleado = request.POST['txtEmpleado']
    cargo = request.POST['txtCargo']

    cliente = Cliente.objects.create(
        cuit = cuit, empresa = empresa, empleado = empleado, cargo = cargo
    )
    messages.success(request, '¡Cliente Registrado!')
    return redirect('/')

def edicionCliente(request, cuit):
    cliente = Cliente.objects.get(cuit = cuit)
    return render(request, "editarCurso.html", {"cliente": cliente})

def eliminarCliente(request, cuit):
    cliente = Cliente.objects.get(cuit = cuit)
    cliente.delete()
    messages.success(request, '¡Cliente Eliminado!')
    return redirect('/')

def editarCliente(request):
    cuit = request.POST['numCuit']
    empresa = request.POST['txtEmpresa']
    empleado = request.POST['txtEmpleado']
    cargo = request.POST['txtCargo']

    cliente = Cliente.objects.get(cuit = cuit)
    cliente.empresa = empresa
    cliente.empleado = empleado
    cliente.cargo = cargo
    cliente.save()
    messages.success(request, '¡Cliente Editado!')
    return redirect('/')
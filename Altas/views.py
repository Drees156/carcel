from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Ppl
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

@login_required(login_url='/login/')
def home(request):
    ppllistados = Ppl.objects.all()
    return render(request, "IngresoAltas.html", {"ppl": ppllistados})

class CustomLoginView(LoginView):
    template_name = 'login.html'

from django.contrib import messages

def user_login(request):
    user = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido, {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, inténtelo de nuevo.')

    return render(request, 'login.html', {'user': user})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login/')
def registrarPpl(request):
    apellidos_nombres=request.POST['txtApellidos_Nombres']
    nu=request.POST['txtNU']
    patio=request.POST['txtPatio']

    ppl=Ppl.objects.create(
        apellidos_nombres=apellidos_nombres, nu=nu, patio=patio)
    messages.success(request, 'PPL Registrado')
    return redirect('/home')

@login_required(login_url='/login/')
def edicionPpl(request, nu):
    ppl = Ppl.objects.get(nu=nu)
    return render(request, "edicionPpl.html", {"ppl":ppl})

@login_required(login_url='/login/')
def editarPpl(request):
    apellidos_nombres=request.POST['txtApellidos_Nombres']
    nu=request.POST['txtNU']
    patio=request.POST['txtPatio']
    
    ppl = Ppl.objects.get(nu=nu)
    ppl.apellidos_nombres = apellidos_nombres
    ppl.patio = patio
    ppl.save()
    messages.success(request, 'PPL Actualizado')
    return redirect('/home')

@login_required(login_url='/login/')
def eliminarPpl(request, nu):
    ppl = Ppl.objects.get(nu=nu)
    ppl.delete()
    messages.success(request, 'PPL Eliminado')
    return redirect('/home')
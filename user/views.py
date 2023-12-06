from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if (request.method == 'GET'):
        return render(request, 'cadastro.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(username=nome).first()
        if user:
            return HttpResponse('já registrado')
        else:
            user = User.objects.create_user(username=nome, email=email, password=senha)
            user.save()
            return HttpResponse("Usuario Cadastrado com Sucesso")

def log(request):
    if(request.method == 'GET'):
        return render(request, 'login.html')
    else:
        username = request.POST.get('nome')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        if user:
            login(request, user)
            return HttpResponse('autenticado')
        else:
            return HttpResponse('email ou senha inválidos')

@login_required(login_url='/auth/login/')
def plataforma(request):
    return HttpResponse('Plataforma')
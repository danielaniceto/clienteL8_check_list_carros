from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.http import HttpRequest

@require_http_methods(['GET', 'POST'])
def login_view(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Por favor, preencha todos os campos.')
        else:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                
                redirect_url = request.GET.get('next', 'home')
                return redirect(redirect_url)
            else:
                messages.error(request, 'Credenciais inválidas. Tente novamente.')

    return render(request, 'login.html')

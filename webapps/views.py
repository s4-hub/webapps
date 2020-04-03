from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .form import UsersForm

@login_required(login_url='login')
def index(request):

    return render(request, 'index.html')

def signin(request):

    if request.method == 'POST':
        form = UsersForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            messages.success(request, f'Selamat Datang {username}')
            return redirect('home')
        else:
            messages.error(request, f'Username atau password anda salah')
            return redirect ('login')
    else:
        form = UsersForm()

    return render(request, 'login.html', {'form':form})

def singout(request):

    logout(request)
    messages.add_message(request, messages.INFO, 'Akun anda berhasil keluar')
    return redirect('login')
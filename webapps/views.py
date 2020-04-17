from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .form import UsersForm
# from absensi_apps.form import KaryawanForm
# from absensi_apps.models import Karyawan

@login_required(login_url='login')
def index(request):
    

    return render(request, 'absensi/index.html')

def register(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('login')
    else:
        form = UsersForm()
    return render(request, 'register.html',{'form':form})

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

# def navbar(request):

#     cuser = request.user
#     admin = User.objects.filter(username=cuser,is_superuser=True)

#     return render(request, 'navbar.html', {'admin':admin}) 
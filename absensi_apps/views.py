from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Scan_Absen, Nik
from .form import ScanForm
import datetime
# Create your views here.

@login_required(login_url='login')
def index(request):
    
    cuser = request.user
    admin = User.objects.filter(username=cuser,is_superuser=True)
    if admin:
        datas = Scan_Absen.objects.all().order_by('user__first_name')

        return render(request, 'absensi_apps/index.html', {'datas':datas})
    else:
        datas = Scan_Absen.objects.select_related('user').filter(user_id=cuser)
        nama = User.objects.filter(username=cuser)

        args = {
            'cuser':cuser,
            'datas':datas,
            'nama':nama
        
        }
        
        return render(request, 'absensi_apps/index.html', args)

@login_required(login_url='login')
def Scan(request):

    cuser = request.user
    # niks = Nik.objects.select_related('user').filter(user__username=cuser).first()
    nama = User.objects.filter(username=cuser)
    nik = Nik.objects.get(user=request.user) 

    if request.method == 'POST':
        
        form = ScanForm(request.POST)
        # print(form)
        
        if form.is_valid:
            post = form.save(commit=False)
            post.user = request.user
            post.nik = nik
            post.save()

            return HttpResponseRedirect(reverse('absensi:list'))
        
    else:
        form = ScanForm()
        cuser = request.user
    return render(request, 'absensi_apps/absen.html', {'form':form, 'cuser':cuser, 'nik':nik, 'nama':nama})


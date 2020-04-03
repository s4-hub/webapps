from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Scan_Absen
from .form import ScanForm
import datetime
# Create your views here.

def index(request):
    
    cuser = request.user
    datas = Scan_Absen.objects.select_related('user').filter(user_id=cuser)
    # args = {
    #     # 'user':request.user,
        
    #     'datas':Scan_Absen.objects.select_related('Scan_Absen', 'Karyawan', 'User')
    # }
    
    return render(request, 'absensi_apps/index.html', {'datas':datas, 'cuser':cuser})

def Scan(request):
    if request.method == 'POST':
        
        form = ScanForm(request.POST)
        # print(form)
        
        if form.is_valid:
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('absensi:list')
        
    else:
        form = ScanForm()
        cuser = request.user
    return render(request, 'absensi_apps/absen.html', {'form':form, 'cuser':cuser})

# def keluar(request):
#     form = KeluarForm(request.POST)
#     if form.is_valid():
#         form.save()
#         form = KeluarForm()

#         return redirect('absensi:absen')

#     args = {'form':form, 'cuser':request.user}
#     return render(request, 'absensi_apps/absen.html', args)


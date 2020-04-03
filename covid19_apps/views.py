from django.shortcuts import render
from .form import KendalaForm
from .models import Kendala
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    
    datas = Kendala.objects.all()

    return render(request, 'index.html',{'datas':datas})

def daftar(request):
    if request.method == 'POST':
        form = KendalaForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.save()

            return HttpResponseRedirect(reverse('kendala:list'))
    else:
        form = KendalaForm()

    return render(request, 'covid19_apps/daftar.html')
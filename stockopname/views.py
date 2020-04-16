from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from .form import PermintaanForm, ProdukForm
from .models import *
from django.views import View
# Create your views here.

@login_required(login_url='login')
class AppStok(View):
    def index(request):

        # datas = SisaStok.objects.all()
        datas = Produk.objects.all()

        return render(request,'apps/index.html', {'datas':datas, 'cuser':request.user})

    def InputProduk(request):
        if request.method == 'POST':
            form = ProdukForm(request.POST)
            if form.is_valid:
                post = form.save(commit=False)
                post.user = request.user
                post.save()

                return HttpResponseRedirect(reverse('stockopname:list'))
        else:
            form = ProdukForm()
        return render(request, 'apps/input.html',{'form':form})
    
    def PermintaanProduk(request, pk):
        prod = Produk.objects.get(pk=pk)
        # perm = Permintaan.objects.get(pk=pk)
        if Permintaan.objects.all() is None:
            Permintaan.objects.create(pk=pk)
        # prod = Permintaan.objects.select_related('produk').get(pk=pk)
        # prod = Produk.objects.all().get(pk=1)
        # data = get_object_or_404(Produk, pk=pk)
            if request.method == 'POST':
                # prod = Permintaan.objects.create(pk=1)
                form = PermintaanForm(request.POST, pk=prod.id)
                if form.is_valid:
                    post = form.save(commit=False)
                    # post.produk = prod.id
                    # print(post.produk)
                    post.user = request.user
                    post.save()

                    return HttpResponseRedirect(reverse('stockopname:list'))
                else:

                    form = PermintaanForm(pk=prod.id)
                    args = {'form':form}
                return render(request, 'apps/permintaan.html',args, pk=prod.id)

    def Stoksisa(request):

        datas = SisaStok.objects.all()

        return render(request,'apps/sisa.html',{'datas':datas})    




from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.urls import reverse
from django.contrib.auth.models import User
from .form import PermintaanForm, ProdukForm
from .models import *
from django.views import View
# Create your views here.

# @login_required(login_url='login')
# @method_decorator(login_required, name='login')
class AppStok(View):
    # login_url = 'login/'
    # redirect_field_name = 'login/'
    @login_required(login_url='login')
    def index(request):

        # datas = SisaStok.objects.all()
        datas = Produk.objects.all()

        return render(request,'apps/index.html', {'datas':datas, 'cuser':request.user})
    
    def permintaan_list(request):

        cuser = request.user
        datas = Permintaan.objects.select_related('produk').all()
        return render(request, 'apps/permintaan_list.html', {'datas':datas, 'cuser':cuser})

    @login_required(login_url='login')
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
    
    @login_required(login_url='login')
    def PermintaanProduk(request, pk):
        
        cuser = request.user
        data = get_object_or_404(Produk, pk=pk)
        if request.method == 'POST':
            
            form = PermintaanForm(request.POST)
            # print(form)
            
            if form.is_valid:
                post = form.save(commit=False)
                post.user = request.user
                post.produk_id = data.pk
                post.save()

                return HttpResponseRedirect(reverse('stockopname:permintaan_list'))
            
        else:
            form = PermintaanForm()
            cuser = request.user
        return render(request, 'apps/permintaan.html', {'form':form, 'cuser':cuser, 'data':data.nama})
    
    @login_required(login_url='login')
    def sisa_stok(request):

        datas = Permintaan.objects.select_related('produk').all()
        return render(request, 'apps/sisa.html', {'datas':datas})

    def autocompleteModel(request):
        if request.is_ajax():
            q = request.GET.get('term', '').capitalize()
            search_qs = Mas.objects.filter(name__startswith=q)
            results = []
            print(q)
            for r in search_qs:
                results.append(r.FIELD)
            data = json.dumps(results)
        else:
            data = 'fail'
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)




from django import forms
from .models import Produk, Permintaan


class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = (
            'kategori','nama',
            'jumlah','satuan',
            'harga','per_unit',
        )

        widgets = {
            'kategori':forms.Select(
                attrs={'class':'form-control'}),
            'nama':forms.TextInput(
                attrs={'class':'form-control',
                'placeholder':'Input Nama Produk',
                'name':'nama'}),
            'jumlah':forms.TextInput(
                attrs={'class':'form-control',
                'placeholder':'Input Jumlah Produk',
                'name':'numeric','id':'numeric'}),
            'per_unit':forms.TextInput(
                attrs={'class':'form-control',
                'placeholder':'Jumlah item per unit ..'}),
            'satuan':forms.Select(
                attrs={'class':'form-control'}),
            'harga':forms.TextInput(
                attrs={'class':'form-control',
                'placeholder':'Input Harga per Item'}),
            
        }


class PermintaanForm(forms.ModelForm):
    class Meta:
        model = Permintaan
        fields = ('jumlah',)

        widgets = {
            'jumlah':forms.TextInput(
                attrs={'class':'form-control',
                'placeholder':'Jumlah item yang direquest..'}),
            
            
        }
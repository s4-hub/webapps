from django import forms
from .models import *


class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = (
            'kategori','nama',
            'jumlah','satuan',
            'harga',
        )

        widgets = {
            'kategori':forms.Select(
                attrs={'class':'form-control'}),
            'nama':forms.TextInput(
                attrs={'class':'form-control',
                'placeholder':'Input Nama Produk'}),
            'jumlah':forms.TextInput(
                attrs={'class':'form-control',
                'placeholder':'Input Jumlah Produk',
                'name':'numeric','id':'numeric'}),
            'satuan':forms.Select(
                attrs={'class':'form-control'}),
            'harga':forms.TextInput(
                attrs={'class':'form-control',
                'placeholder':'Input Harga per Item'}),
            
        }


class PermintaanForm(forms.ModelForm):
    class Meta:
        model = Permintaan
        fields = ('jumlah', 'produk')

        widgets = {
            'jumlah':forms.TextInput(
                attrs={'class':'form-control'}),
            'produk':forms.Select(
                attrs={'class':'form-control'})
            
        }
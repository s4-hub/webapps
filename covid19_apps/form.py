from django import forms
from .models import Kendala

class KendalaForm(forms.ModelForm):
    class Meta:
        model = Kendala
        fields = [
            'tgl_kendala',
            'bidang',
            'keterangan',
        ]

        widgets = {
            'tgl_kendala':forms.TextInput(
                attrs={'class':'form-control',
                'name':'tgl[]'}),
            'bidang':forms.Select(
                attrs={'class':'form-control',
                'name':'bidang[]'}),
            'keterangan':forms.Textarea(
                attrs={'class':'form-control',
                'name':'ket[]',
                'placholder':'Input Keterangan...'}),
        }
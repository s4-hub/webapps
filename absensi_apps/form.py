from django import forms
from .models import Scan_Absen


class ScanForm(forms.ModelForm):
    class Meta:
        model = Scan_Absen
        fields = ('pilihan',)

        widgets = {
            'pilihan':forms.Select(
                attrs={'class':'form-control'}),
        }
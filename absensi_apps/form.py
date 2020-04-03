from django import forms
from .models import Scan_Absen, Nik

class ScanForm(forms.ModelForm):
    class Meta:
        model = Scan_Absen
        fields = ('pilihan',)

        widgets = {
            
            'pilihan': forms.Select(
                attrs={'class': 'form-control'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['nik'].queryset = Nik.objects.none()
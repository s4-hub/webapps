from django.contrib.auth.models import User
from django import forms

class UsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username','password'
        ]

        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control',
                'placeholder': 'Masukkan Username',
                'type': 'username', 'required':''}),
            'password': forms.TextInput(
                attrs={'class': 'form-control',
                'placeholder': 'Masukkan Password',
                'type': 'password', 'required':''}),
        }
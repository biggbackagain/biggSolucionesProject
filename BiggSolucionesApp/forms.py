# core/forms.py

from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nombre','apellido', 'correo', 'telefono','mensaje',]
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingresa tu nombre'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Ingresa tu apellido'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'Ingresa tu email'}),
            'telefono':forms.TextInput(attrs={'placeholder': 'Ingresa tu telefono'}),
            'mensaje': forms.Textarea(attrs={'rows': 10, 'placeholder': 'Ingresa tu mensaje'}),
        }

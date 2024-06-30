# core/views.py

from django.shortcuts import render, redirect
from .forms import ContactForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print("Formulario válido y guardado")
            return redirect('/')  # Redirige a la misma página para mostrar el formulario vacío de nuevo
        else:
            print("Errores de formulario:", form.errors)
    else:
        form = ContactForm()
    
    return render(request, 'index.html', {'form': form})
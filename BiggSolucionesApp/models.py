from django.db import models

class Contact(models.Model):
    nombre = models.CharField(max_length=100, default='')
    apellido = models.CharField(max_length=100, default='')
    telefono= models.CharField(max_length=100, default='')
    correo = models.EmailField()
    mensaje = models.TextField()
    

    def __str__(self):
        return self.nombre, self.apellido, self.telefono, self.correo, self.mensaje
# Generated by Django 4.2.13 on 2024-06-30 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BiggSolucionesApp', '0004_rename_email_contact_correo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='apellido',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='telefono',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='nombre',
            field=models.CharField(default='', max_length=100),
        ),
    ]

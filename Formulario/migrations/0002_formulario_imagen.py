# Generated by Django 3.2.9 on 2021-11-14 05:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Formulario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario',
            name='imagen',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='productos'),
            preserve_default=False,
        ),
    ]

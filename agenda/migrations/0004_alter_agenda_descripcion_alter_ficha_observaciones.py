# Generated by Django 4.2.1 on 2023-05-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_agenda_fecha_agenda_hora_ficha_peso_ficha_talla'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='descripcion',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='observaciones',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]

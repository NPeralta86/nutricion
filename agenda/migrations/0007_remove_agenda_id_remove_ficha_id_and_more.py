# Generated by Django 4.2.1 on 2023-05-14 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0006_alter_pacientes_genero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='id',
        ),
        migrations.RemoveField(
            model_name='ficha',
            name='id',
        ),
        migrations.AlterField(
            model_name='agenda',
            name='paciente',
            field=models.CharField(max_length=11, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='fecha',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='paciente',
            field=models.CharField(max_length=11, primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-21 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agenda', '0008_agenda_id_ficha_id_alter_agenda_paciente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-21 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_rename_extintores_vistoriasrealizadas_extintor'),
    ]

    operations = [
        migrations.AddField(
            model_name='vistoriasrealizadas',
            name='vistoria_agendada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.vistoriasagendadas'),
        ),
    ]
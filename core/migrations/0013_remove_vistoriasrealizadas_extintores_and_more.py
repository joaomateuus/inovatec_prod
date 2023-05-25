# Generated by Django 4.2.1 on 2023-05-21 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_vistoriasagendadas_vistoriasrealizadas_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vistoriasrealizadas',
            name='extintores',
        ),
        migrations.AddField(
            model_name='vistoriasrealizadas',
            name='extintores',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.extintor'),
        ),
    ]

# Generated by Django 4.2 on 2023-04-26 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_extintor_qrcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extintor',
            name='qrcode_link',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Link do Qrcode'),
        ),
        migrations.AlterField(
            model_name='qrcode',
            name='qrcode_link',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Link do Qrcode'),
        ),
    ]
# Generated by Django 4.2 on 2023-04-26 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_extintor_qrcode_link_remove_qrcode_extintor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='qrcode_link',
            field=models.CharField(max_length=50, verbose_name='Link do Qrcode'),
        ),
    ]

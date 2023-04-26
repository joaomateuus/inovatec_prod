from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from core import models
from .qrcode import qrcode_generator as qrcode_provider

@receiver(post_save, sender=models.Extintor)
def create_qrcode_for_extinguisher(sender, instance: models.Extintor, created, **kwargs):
    if created: 
        try: 
            qr_code, qrcode_link = qrcode_provider.qrcode_generator(instance)
            
            qrcode_instance = models.Qrcode.objects.create(
                image=qr_code,
                qrcode_link=qrcode_link
            )
            
            models.Extintor.objects.filter(id=instance.id).update(
                qrcode=qrcode_instance
            )
        except Exception as e:
            print(f"Error on qrcode genration -> {e}")
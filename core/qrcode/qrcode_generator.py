from io import BytesIO
from core import models
from django.core.files.uploadedfile import InMemoryUploadedFile
import qrcode

def qrcode_generator(instance: models.Extintor):
    url_qrcode = f'https://localhost:3000/extintores/{instance.id}'
    qr_code = qrcode.make(url_qrcode)
        
    qrcode_buffer = BytesIO()
    qr_code.save(qrcode_buffer, format='PNG')
    qrcode_buffer.seek(0)
        
    in_memory_file = InMemoryUploadedFile(
        qrcode_buffer,
        None,
        f'{instance.id}-{instance.codigo}_qrcode.png',
        'image/png',
        qrcode_buffer.tell(),
        None
    )
    return in_memory_file, url_qrcode
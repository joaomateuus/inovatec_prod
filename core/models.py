from django.db import models
from django.contrib.auth import get_user_model

Usuario = get_user_model()

# Create your models here.
class Estabelecimento(models.Model):
    nome = models.CharField(
        'Nome',
        max_length=100
    )
    
    cnpj = models.CharField(
        'CNPJ',
        max_length=30
    )
    
    contato = models.CharField(
        'Contato',
        max_length=30
    )
    
    endereco = models.TextField(
        'Endereco'
    )
    
    area_atuacao = models.CharField(
        'Area de atuacao',
        max_length=50
    )
    
    def __str__(self) -> str:
        return f"{self.cnpj} - {self.nome}"
    
    class Meta:
        db_table = 'tb_estabelecimentos'


class Extintor(models.Model):
    codigo = models.CharField(
        max_length=30,
    )
    data_validade = models.DateField()
    nivel = models.CharField(
        'Nivel Extintor',
        max_length=50
    )
    
    termo_garantia = models.BooleanField(
        'Termo de Garantia'
    )
    
    tipo = models.CharField(
        'Tipo de Extintor',
        max_length=50
    )
    
    tamanho = models.CharField(
        'Tamanho do extintor',
        max_length=50
    )
    
    local = models.CharField(
        'Local do Extintor',
        max_length=100
    )
    
    estabelecimento = models.ForeignKey(
        Estabelecimento,
        on_delete=models.CASCADE,
    )
    
    qrcode = models.ImageField(
        upload_to='images/qrcode',
        blank=True,
        null=True,
    )
    
    qrcode_link = models.CharField(
        'Link do Qrcode',
        max_length=30,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return f"{self.id} - {self.tipo}"
    
    class Meta:
        db_table = 'tb_extintores'


class Vistoria(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING
    )
    
    extintor = models.ForeignKey(
        Extintor,
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING
    )
    
    data = models.DateField()
    informacoes = models.TextField()
    
    def __str__(self):
        return f"{self.extintor.codigo} - {self.data}"
    
    class Meta:
        db_table = 'tb_vistorias'
    
    
class Qrcode(models.Model):
    extintor = models.ForeignKey(
        Extintor,
        related_name='extintor_qr',
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    
    qrcode = models.ImageField(
        upload_to='images/qrcode',
        blank=False,
        null=False
    )
    
    qrcode_link = models.CharField(
        'Link do Qrcode',
        max_length=30,
        null=False,
        blank=False
    )
    
    def __str__(self):
        return f"{self.id} - {self.extintor.codigo}"
    
    class Meta:
        db_table = 'tb_qrcodes'
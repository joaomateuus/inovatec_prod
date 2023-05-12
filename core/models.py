from django.db import models
from django.contrib.auth import get_user_model

Usuario = get_user_model()

# Empresa a ser vistoriada
class Empresa(models.Model):
    nome = models.CharField(
        'Nome',
        max_length=100,
        null=True,
        blank=True,
    )
    cnpj = models.CharField(
        'CNPJ',
        max_length=30,
        null=True,
        blank=True,
    )
    contato = models.CharField(
        'Contato',
        max_length=30,
        null=True,
        blank=True,
    )
    endereco = models.TextField(
        'Endereco',
        null=True,
        blank=True,
    )
    area_atuacao = models.CharField(
        'Area de atuacao',
        max_length=50,
        null=True,
        blank=True,
    )
    
    def __str__(self) -> str:
        return f"{self.cnpj} - {self.nome}"
    
    class Meta:
        db_table = 'tb_empresas'

class Qrcode(models.Model):   
    image = models.ImageField(
        'Qrcode Imagem', 
        upload_to='images/qrcode/',
        blank=False,
        null=False
    )
    
    qrcode_link = models.CharField(
        'Link do Qrcode',
        max_length=50,
        null=False,
        blank=False
    )
    
    def __str__(self):
        return f"{self.id} - {self.image}"
    
    class Meta:
        db_table = 'tb_qrcodes'


class Extintor(models.Model):
    codigo = models.CharField(
        'Codigo Extintor',
        max_length=30,
        null=True,
        blank=True
    )
    data_validade = models.DateField(
        'Data de validade',
        null=True,
        blank=True
    )
    nivel = models.CharField(
        'Nivel Extintor',
        max_length=50,
        null=True,
        blank=True
    )
    termo_garantia = models.BooleanField(
        'Termo de Garantia',
        null=True,
        blank=True
    )
    tipo = models.CharField(
        'Tipo de Extintor',
        max_length=50,
        null=True,
        blank=True
    )
    tamanho = models.CharField(
        'Tamanho do extintor',
        max_length=50,
        null=True,
        blank=True
    )
    local = models.CharField(
        'Local do Extintor',
        max_length=100,
        null=True,
        blank=True
    )
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    qrcode = models.ForeignKey(
        Qrcode,
        related_name='qrcode_ext',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    
    def __str__(self):
        return f"{self.id} - {self.tipo}"
    
    class Meta:
        db_table = 'tb_extintores'


class Fiscal(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING
    )
    codigo_fiscal = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    empresa_fiscal = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    
    def __str__(self):
        return f"{self.codigo_fiscal} - {self.empresa_fiscal}"
    
    class Meta:
        db_table = 'tb_fiscais'

class Denuncia(models.Model):
    class Status(models.TextChoices):
        ANALISE = 'ANA', ('Análise')
        ANDAMENTO = 'ANDA', ('Andamento')
        CONCLUIDA = 'CONC', ('CONCLUÍDA')
    
    usuario = models.ForeignKey(
        Usuario,
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING
    )
    numero_protocolo = models.CharField(
        max_length=20,
        unique=True,
        editable=False
    )
    dt_denuncia = models.DateField(
        auto_now_add=True,
        null=True,
        blank=True,
    )
    local_ocorrencia = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    descricao = models.TextField(
        null=True,
        blank=True
    )
    anexo = models.ImageField(
        upload_to='images/denuncias/',
        blank=True,
        null=True
    )
    status = models.CharField(
        'Status',
        max_length=5,
        choices=Status.choices,
        default=Status.ANALISE
    )
    
    def save(self, *args, **kwargs):
        if not self.numero_protocolo:
            self.numero_protocolo = self.generate_protocol_number()
        
        return super().save(*args, **kwargs)
    
    def generate_protocol_number(self):
        protocol = f"{self.dt_denuncia} - {self.local_ocorrencia}"
        return protocol
    
    def __str__(self):
        return f"{self.numero_protocolo}"
    
    class Meta:
        db_table = 'tb_denuncias'
    
    
class Vistoria(models.Model):
    fiscal = models.ForeignKey(
        Fiscal,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING
    )
    denuncia = models.ForeignKey(
        Denuncia,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING
    )
    empresa = models.ForeignKey(
        Empresa,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING
    )
    extintor = models.ForeignKey(
        Extintor,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING
    )
    data_agendada = models.DateField(
        null=True,
        blank=True
    )
    data_realizada = models.DateField(
        null=True,
        blank=True
    )
    informacoes = models.TextField(
        null=True,
        blank=True,
    )
    resultado = models.TextField(
        null=True,
        blank=True,
    )
    
    def __str__(self):
        return f"{self.extintor.codigo} - {self.data}"
    
    class Meta:
        db_table = 'tb_vistorias'


    
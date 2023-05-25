import base64
import datetime
from rest_framework import serializers
from core import models
from django.core.files.base import ContentFile

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Empresa
        fields = '__all__'

class QrocdeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Qrcode
        fields = '__all__'

class ExtintorSerializer(serializers.ModelSerializer):
    qrcode = QrocdeSerializer(read_only=True)
    empresa_nome = serializers.CharField(source='empresa.nome', read_only=True)
    
    
    class Meta:
        model = models.Extintor
        fields = '__all__'
        
    
class FiscalSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Fiscal
        fields = '__all__'
    
class DenunciaSerializer(serializers.ModelSerializer):
    anexo = serializers.CharField()
    usuario_nome = serializers.CharField(source='usuario.nome')
    
    def create(self, validated_data):
        image_data = validated_data.pop('anexo', None)
        instance = super().create(validated_data)

        if image_data:
            data = base64.b64decode(image_data)
            instance.anexo.save(f'{datetime.date.today()} - {instance.local_ocorrencia}.jpg', ContentFile(data), save=True)
        
        return instance
    
    class Meta:
        model = models.Denuncia
        fields = '__all__'

class VistoriasAgendadasSerializer(serializers.ModelSerializer):
    empresa_agendada = serializers.SerializerMethodField()
    
    def get_empresa_agendada(self, obj):
        return f"{obj.empresa.cnpj} - {obj.empresa.nome}"
    
    class Meta:
        model = models.VistoriasAgendadas
        fields = '__all__'

class VistoriasRealizadasSerializer(serializers.ModelSerializer):
    fiscal_nome = serializers.CharField(source='fiscal.usuario.nome', read_only=True)
    extintor_codigo = serializers.CharField(source='extintor.codigo', read_only=True)
    anexos_img = serializers.CharField()

    def create(self, validated_data):
        image_data = validated_data.pop('anexos_img', None)
        instance = super().create(validated_data)

        if image_data:
            data = base64.b64decode(image_data)
            instance.anexos_img.save(f'{datetime.date.today()} - {instance.extintor.codigo}.jpg', ContentFile(data), save=True)

        return instance

    class Meta:
        model = models.VistoriasRealizadas
        fields = '__all__'
            
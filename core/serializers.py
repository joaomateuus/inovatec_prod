from rest_framework import serializers
from core import models
from account.serializers import UsuarioSerializer
from account import models as auth_models

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
    
    class Meta:
        model = models.Extintor
        fields = '__all__'

class FiscalSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Fiscal
        fields = '__all__'
    
class DenunciaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Denuncia
        fields = '__all__'
        
class VistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vistoria
        fields = '__all__'

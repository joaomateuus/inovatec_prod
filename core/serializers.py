from rest_framework import serializers
from core import models

class EstabelecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Estabelecimento
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

class VistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vistoria
        fields = '__all__'
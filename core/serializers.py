from rest_framework import serializers
from core import models

class EstabelecimentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Estabelecimento
        fields = '__all__'

class ExtintorSerializer(serializers.ModelSerializer):
    qrcode = serializers.ImageField(
        read_only=True
    )
    qrcode_link = serializers.CharField(
        read_only=True
    )
    
    class Meta:
        model = models.Extintor
        fields = '__all__'

class VistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vistoria
        fields = '__all__'

class QrocdeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Qrcode
        fields = '__all__'
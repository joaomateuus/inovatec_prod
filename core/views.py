from rest_framework import viewsets
from core import models
from core import serializers

class EstabelecimentoViewSet(viewsets.ModelViewSet):
    queryset = models.Estabelecimento.objects.all()
    serializer_class = serializers.EstabelecimentoSerializer

class ExtintorViewSet(viewsets.ModelViewSet):
    queryset = models.Extintor.objects.all()
    serializer_class = serializers.ExtintorSerializer

class VistoriaViewSet(viewsets.ModelViewSet):
    queryset = models.Vistoria.objects.all()
    serializer_class = serializers.VistoriaSerializer

class QrcodeViewSet(viewsets.ModelViewSet):
    queryset = models.Qrcode.objects.all()
    serializer_class = serializers.QrocdeSerializer


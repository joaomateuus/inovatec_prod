from rest_framework import viewsets
from core import models
from core import serializers
from account import serializers as account_serializers
from rest_framework.response import Response
from rest_framework import status

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = models.Empresa.objects.all()
    serializer_class = serializers.EmpresaSerializer

class ExtintorViewSet(viewsets.ModelViewSet):
    queryset = models.Extintor.objects.all()
    serializer_class = serializers.ExtintorSerializer

class VistoriaViewSet(viewsets.ModelViewSet):
    queryset = models.Vistoria.objects.all()
    serializer_class = serializers.VistoriaSerializer

class QrcodeViewSet(viewsets.ModelViewSet):
    queryset = models.Qrcode.objects.all()
    serializer_class = serializers.QrocdeSerializer

class DenunciaViewSet(viewsets.ModelViewSet):
    queryset = models.Denuncia.objects.all()
    serializer_class = serializers.DenunciaSerializer

class FiscalViewSet(viewsets.ModelViewSet):
    queryset = models.Fiscal.objects.all()
    serializer_class = serializers.FiscalSerializer
    
    def create(self, request, *args, **kwargs):
        try:
            user_data = request.data.pop('user_data', {})
            
            user_serializer = account_serializers.UsuarioSerializer(data=user_data)
            user_serializer.is_valid(raise_exception=True)
            usuario = user_serializer.save()
            
            request.data['usuario'] = usuario.id
            
            fiscal_serializer = self.serializer_class(data=request.data)
            fiscal_serializer.is_valid(raise_exception=True)
            fiscal_serializer.save()
            
            response_data = {
                'usuario': user_serializer.data,
                'fiscal': fiscal_serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

    
    


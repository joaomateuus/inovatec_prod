from rest_framework import viewsets
from core import models
from core import serializers
from account import serializers as account_serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import permissions
from rest_framework.decorators import action

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = models.Empresa.objects.all()
    serializer_class = serializers.EmpresaSerializer
    permission_classes = (IsAuthenticated,)
    
class ExtintorViewSet(viewsets.ModelViewSet):
    queryset = models.Extintor.objects.all()
    serializer_class = serializers.ExtintorSerializer
    permission_classes = (AllowAny,)
    
class VistoriaAgendadaViewSet(viewsets.ModelViewSet):
    queryset = models.VistoriasAgendadas.objects.all()
    serializer_class = serializers.VistoriasAgendadasSerializer
    permission_classes = (IsAuthenticated,)

class VistoriaRealizadaViewSet(viewsets.ModelViewSet):
    queryset = models.VistoriasRealizadas.objects.all()
    serializer_class = serializers.VistoriasRealizadasSerializer 
    permission_classes = (IsAuthenticated,)
       
class QrcodeViewSet(viewsets.ModelViewSet):
    queryset = models.Qrcode.objects.all()
    serializer_class = serializers.QrocdeSerializer

class DenunciaViewSet(viewsets.ModelViewSet):
    queryset = models.Denuncia.objects.all()
    serializer_class = serializers.DenunciaSerializer
    
    permission_classes_by_action = {
        'create': [permissions.IsAuthenticated],
        'list': [permissions.AllowAny],
        'update': [permissions.IsAdminUser],    
        'destroy': [permissions.IsAdminUser]
    }

class FiscalViewSet(viewsets.ModelViewSet):
    queryset = models.Fiscal.objects.all()
    serializer_class = serializers.FiscalSerializer
    permission_classes_by_action = {
        'create': [permissions.AllowAny],
        'list': [permissions.IsAuthenticated],
        'update': [permissions.IsAuthenticated],    
        'destroy': [permissions.IsAuthenticated]
    }
    
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
        
    @action(detail=False, methods=['post'])
    def get_fiscal_by_user_id(self, request, **kwargs):
        # print(request.data)
        # user_id = request.data['user_id']
        user_id = self.request.query_params.get('user')
        
        user = models.Fiscal.objects.filter(usuario=user_id).first()
        if user is not None:
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=200)
        else:
            return Response({'error': 'Usuário não encontrado.'}, status=404)
        
        
        
    
    


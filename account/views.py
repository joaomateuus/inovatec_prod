from rest_framework import viewsets
from account import models
from account import serializers
from rest_framework import permissions

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer
    permission_classes_by_action = {
        'create': [permissions.AllowAny],
        'list': [permissions.IsAuthenticated],
        'update': [permissions.IsAuthenticated],    
        'destroy': [permissions.IsAuthenticated]
    }
    
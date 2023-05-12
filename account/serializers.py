from rest_framework import serializers
from account import models

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style = {'input_type': 'password'},
        write_only = True,
        label = 'Senha'
    )
    password_confirm = serializers.CharField(
        style = {'input_type': 'password'},
        write_only = True,
        label = 'Confirme a Senha'
    )
    is_staff = serializers.BooleanField( 
        label="Usuário Admin",
        help_text="Indica que usuário consegue acessar a página de administração."
    )
    is_superuser = serializers.BooleanField(
        label="Super Usuário",
        help_text="Indica que este usuário tem todas as permissões do sistema"
    )
    last_login = serializers.DateTimeField(
        read_only=True
    )
    
    def save(self):
        password = self.validated_data['password']
        password_confirm = self._validated_data.pop('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError({'password': 'As senhas não são iguais.'})
        obj = models.Usuario(**self.validated_data)
        obj.set_password(password)
        obj.save()
        return obj
    
    class Meta:
        model = models.Usuario
        fields = (
            'id', 'username','nome', 'email','cpf', 'is_fiscal', 'numero_telefone',
            'password', 'password_confirm', 'is_staff', 'is_superuser', 'last_login' 
        )
from django.contrib.auth.base_user import BaseUserManager

class UsersManager(BaseUserManager):
    def _create_user(self, username, nome, password, **extra_fields):
        if not username or not nome:
            raise ValueError('There are missing informations')
        username = self.model.normalize_username(username)
        user = self.model(username=username, nome=nome, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, nome=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, nome, password, **extra_fields)
    
    def create_superuser(self, username, nome=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self._create_user(username, nome, password, **extra_fields)
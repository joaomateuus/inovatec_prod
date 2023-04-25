from django.urls import path
from rest_framework.routers import DefaultRouter
from account import views

router = DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet, basename='usuarios')

urlpatterns = router.urls
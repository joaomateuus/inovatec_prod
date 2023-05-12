from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter()
router.register(r'empresas', views.EmpresaViewSet, basename='estabelecimentos')
router.register(r'extintores', views.ExtintorViewSet, basename='extintores')
router.register(r'denuncias', views.DenunciaViewSet, basename='denuncias')
router.register(r'vistorias', views.VistoriaViewSet, basename='vistorias')
router.register(r'fiscais', views.FiscalViewSet, basename='fiscal')
router.register(r'qrcodes', views.QrcodeViewSet, basename='qrcodes')

urlpatterns = router.urls
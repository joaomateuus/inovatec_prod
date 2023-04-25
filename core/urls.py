from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter()
router.register(r'estabelecimentos', views.EstabelecimentoViewSet, basename='estabelecimentos')
router.register(r'extintores', views.ExtintorViewSet, basename='extintores')
router.register(r'vistorias', views.VistoriaViewSet, basename='vistorias')
router.register(r'qrcodes', views.QrcodeViewSet, basename='qrcodes')

urlpatterns = router.urls
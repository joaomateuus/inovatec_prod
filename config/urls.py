from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('api/v1/', include('core.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
]  

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

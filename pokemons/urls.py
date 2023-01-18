from core.views import random_number_view
from core.views.user import RegistrationView

from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="Pokemon API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.ourapp.com/policies/terms/",
      contact=openapi.Contact(email="juanlondono151776@hotmail.com"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'api/v1/', include('core.urls')),

    path("api/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path('api/register/', RegistrationView.as_view(), name='register'),
    path('api/random_number/', random_number_view, name='random_number'),

    # Schema Generation
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

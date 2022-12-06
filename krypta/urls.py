from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Travel API",
        default_version='v1',
        description="My travels site api",
        terms_of_service="",
        contact=openapi.Contact(email="atashbaevnurjigit@gmail.com"),
        license=openapi.License(name="My License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('valuta/', include('valuta.urls')),
    path('wallet/', include('wallet.urls')),

]

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

API_TITLE = 'Locaion API'
API_DESCRIPTION = 'A Web API for list of available Locations'

schema_view = get_schema_view(
    openapi.Info(
        title="Locaion API",
        default_version='v1',
        description="A Web API for list of available Locations"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION, permission_classes=(permissions.AllowAny,))),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

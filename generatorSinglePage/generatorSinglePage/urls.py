from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core import urls as core_urls
from generator import urls as generator_urls
from . import views


urlpatterns = [
    path('', include(core_urls)),
    path('', include(generator_urls)),
    path('admin/', admin.site.urls),
    path('update_server/', views.update, name='update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
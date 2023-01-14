from django.conf import settings
from django.conf.urls import include
from django.urls import path, re_path
from django.views.static import serve

from core.apps import CoreConfig

from .routes import ApiRouter

app_name = CoreConfig.name

urlpatterns = [
    path('', include(ApiRouter.get().urls)),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(
            r'^media(?P<path>.*)$',
            serve,
            {
                'document_root': settings.MEDIA_ROOT,
            },
        ),
    ]

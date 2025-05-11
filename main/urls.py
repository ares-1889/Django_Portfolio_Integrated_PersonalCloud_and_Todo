from django.contrib import admin
from django.urls import path, include
from .views import index, vault, validate_credentials, route, todo, file_upload
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index ),
    path('router/', route, name='router'),
    path('vault/',vault,name='vault'),
    path('todo/',todo,name='todo'),
    path('api/validate', validate_credentials),
    path('api/file_upload', file_upload),
    # path('api/file_download',),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

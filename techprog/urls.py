from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from techprog import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pythonDev.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

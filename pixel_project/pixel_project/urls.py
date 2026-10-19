"""
URL configuration for pixel_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import RedirectView
from django.views.static import serve as static_serve
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.svg'), permanent=True)),
    path('', include('studio.urls')),
    path('admin/', admin.site.urls),
    path('', include('blockchain.urls')),
]

# Fichiers media servis quel que soit DEBUG (les médias sont embarqués dans
# l'image Docker). `static()` ne les sert qu'avec DEBUG=True.
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', static_serve, {'document_root': settings.MEDIA_ROOT}),
]

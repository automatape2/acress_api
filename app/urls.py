"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from app.pea2017.views import index, pea_upload
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pubinei/', include('app.pubinei.urls')),
    path('pea2017/', include('app.pea2017.urls')),
    path('midis/', include('app.midis.urls')),
    path('susalud/', include('app.susalud.urls')),
]

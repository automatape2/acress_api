from django.urls import path
from .views import index, pea_upload

urlpatterns = [
    path('', index, name='pea2017.index'),
    path('upload', pea_upload, name='pea2017.pea_upload'),
]
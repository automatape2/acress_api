from django.urls import path
from .views import index, centros_poblados

urlpatterns = [
    path('', index, name='midis.index'),
    path('centros-poblados', centros_poblados, name='midis.centros_poblados'),
]
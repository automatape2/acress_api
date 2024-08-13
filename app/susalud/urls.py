from django.urls import path
from .views import ipress, establecimientos

urlpatterns = [
    path('ipress', ipress, name='midis.ipress'),
    path('establecimientos', establecimientos, name='midis.establecimientos'),
]
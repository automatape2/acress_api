from django.urls import path
from .views import index, peaCP

urlpatterns = [
    path('peaCP', peaCP, name='pubinei.peaCP'),
    path('', index, name='pubinei.index'),
]
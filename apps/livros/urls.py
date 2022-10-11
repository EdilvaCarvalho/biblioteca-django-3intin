from django.urls import path
from .views import *

urlpatterns = [

    path('', LivrosPublicadoList.as_view(), name='index'),
]
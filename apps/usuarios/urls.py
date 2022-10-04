from django.urls import path
from .views import *

urlpatterns = [
    path('criar/usuario/', UsuarioCreate.as_view(), name='criar_usuario'),
]
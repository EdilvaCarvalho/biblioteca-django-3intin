from django.urls import path
from .views import *

urlpatterns = [
    path('', LivrosPublicadoList.as_view(), name='index'),

    path('criar/editora/', EditoraCreate.as_view(), name='criar_editora'),
    path('listar/editoras/', EditoraList.as_view(), name='listar_editoras'),
]
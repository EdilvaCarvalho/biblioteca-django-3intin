from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('criar/usuario/', UsuarioCreate.as_view(), name='criar_usuario'),
]
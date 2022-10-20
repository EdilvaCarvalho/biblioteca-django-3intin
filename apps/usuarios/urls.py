from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password/', PasswordChangeView.as_view(template_name='cadastros/mudar-senha.html'), name='password'),
    path('criar/usuario/', UsuarioCreate.as_view(), name='criar_usuario'),
    path('editar/usuario/', UsuarioUpdate.as_view(), name='editar_usuario'),
    path('detalhar/usuario/', UsuarioDetail.as_view(), name='detalhar_usuario'),
]
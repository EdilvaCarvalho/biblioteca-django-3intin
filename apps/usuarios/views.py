from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .form import UsuarioForm

class UsuarioCreate(CreateView, SuccessMessageMixin):
    form_class = UsuarioForm
    success_message = 'Usuário criado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Usuários - Biblioteca'
        context['descricao'] = 'Cadastro de Usuário'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class UsuarioUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    form_class = UsuarioForm
    success_message = 'Usuário atualizado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("detalhar_usuario")

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Usuários - Biblioteca'
        context['descricao'] = 'Editar Usuário'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class UsuarioDetail(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = User
    template_name = "cadastros/detalhes/usuario.html"

    def get_object(self, queryset=None):
        return self.request.user

class PasswordChangeView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    login_url = reverse_lazy('login')
    from_class = PasswordChangeView
    success_message = 'Senha alterada com sucesso!'
    success_url = reverse_lazy('index')
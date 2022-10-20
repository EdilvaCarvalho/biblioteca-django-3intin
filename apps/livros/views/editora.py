from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView

from apps.livros.models import Editora


class EditoraCreate(CreateView, SuccessMessageMixin, LoginRequiredMixin):
    login_url = reverse_lazy('login')
    model = Editora
    fields = "__all__"
    success_message = 'Editora criada com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Editoras - Biblioteca'
        context['descricao'] = 'Cadastro de Editora'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class EditoraList(ListView):
    model = Editora
    template_name = "cadastros/listas/editoras.html"
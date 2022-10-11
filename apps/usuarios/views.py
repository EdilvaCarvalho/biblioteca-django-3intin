from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .form import UsuarioForm

class UsuarioCreate(CreateView):
    form_class = UsuarioForm
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")
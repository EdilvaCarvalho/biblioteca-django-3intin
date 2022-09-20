from django.views.generic import ListView
from apps.livros.models import Livro

class LivrosPublicadoList(ListView):
    model = Livro
    template_name = "index.html"


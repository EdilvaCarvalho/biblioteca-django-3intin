from django.views.generic import ListView
from apps.livros.models import Livro

class LivrosPublicadoList(ListView):
    model = Livro
    template_name = "index.html"

    def get_queryset(self):
        return Livro.objects.filter(publicado=True)

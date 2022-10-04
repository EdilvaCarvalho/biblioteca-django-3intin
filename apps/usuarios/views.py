from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class UsuarioCreate(CreateView):
    model = User
    fields = '__all__'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")
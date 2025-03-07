from django.shortcuts import render
from django.views.generic import ListView
from produtos.models import Produto

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/produtos.html'
    context_object_name = 'produtos'
    paginate_by = 10 
    
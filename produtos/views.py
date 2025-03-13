from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from produtos.models import Produto

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/produtos.html'
    context_object_name = 'produtos'
    paginate_by = 10 
    
class ProdutoCreateView(CreateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco', 'quantidadeEstoque','categoria','fornecedor']
    template_name = 'produtos/produto_create_update.html'
    success_url = reverse_lazy('produtos-lista')
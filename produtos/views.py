from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from produtos.models import Produto

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/produtos.html'
    context_object_name = 'produtos'
    paginate_by = 10 
    
class ProdutoCreateView(CreateView):
    model = Produto
    fields = ['nome','marca', 'descricao', 'preco', 'quantidadeEstoque','categoria','fornecedor','imagem','usuario']
    template_name = 'produtos/produto_create_update.html'
    success_url = reverse_lazy('produtos-lista')

class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ['nome','marca', 'descricao', 'preco', 'quantidadeEstoque','categoria','fornecedor','imagem', 'usuario']
    template_name = 'produtos/produto_create_update.html'
    success_url = reverse_lazy('produtos-lista')

class ProdutoDeleteView(DeleteView):
    model=Produto
    success_url=reverse_lazy('produtos-lista')
    template_name = 'produtos/produto_confirm_delete.html'
    context_object_name='produto'
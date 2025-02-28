from django.db import models
from fornecedores.models import Fornecedor
from categorias.models import Categoria

class Produto(models.Model):
    nome = models.CharField(verbose_name='nome do produto', max_length=50, blank=False, null=False )
    descricao=models.CharField(verbose_name='Descrição do Produto', max_length=200)
    preco = models.DecimalField(verbose_name='Preço',  max_digits=10, decimal_places=2, blank=False, null=False)
    quantidadeEstoque=models.PositiveIntegerField(verbose_name='Quantidade em Estoque', default=0 ) 
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT )
    fornecedor= models.ForeignKey(Fornecedor, on_delete=models.PROTECT )
    
    class Meta:
        verbose_name= 'Produto'
        verbose_name_plural = 'Produtos'
        db_table = 'produto'
    
    def __str__(self):
        return self.nome

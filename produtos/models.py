from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
class Categoria(models.Model):
    nome = models.CharField(verbose_name='Categoria do Produto', blank=False, null=False, max_length=200)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table  = 'categoria'
    
    def __str__(self):
        return self.nome

    
class Fornecedor(models.Model):
    nome = models.CharField(verbose_name='Nome Fantasia', max_length=150, blank=False, null=False)
    contato =models.CharField(verbose_name='contato do fornecedor', max_length=15, blank=False, null=False)
    cnpj = models.CharField(verbose_name='cnpj', max_length=14, blank=False, null=False, unique=True)

    class Meta:
        verbose_name='Fornecedor'
        verbose_name_plural='Fornecedores'
        db_table='fornecedor'
        ordering = ['id']

    def __str__(self):
        return (f' {self.nome} - {self.cnpj}')
    

class Produto(models.Model):
    nome = models.CharField(verbose_name='nome do produto', max_length=50, blank=False, null=False )
    descricao=models.CharField(verbose_name='Descrição do Produto', max_length=200)
    preco = models.DecimalField(verbose_name='Preço',  max_digits=10, decimal_places=2, blank=False, null=False)
    quantidadeEstoque=models.PositiveIntegerField(verbose_name='Quantidade em Estoque', default=0 ) 
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT )
    fornecedor= models.ForeignKey(Fornecedor, on_delete=models.PROTECT )
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    imagem = models.ImageField(null=True, blank=True, upload_to='imagens')
    marca = models.CharField(max_length=200, null=True, blank=True)
    avaliacao = models.DecimalField(max_digits=10,decimal_places=2, null=True, blank=True)
    criadoEm = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        verbose_name= 'Produto'
        verbose_name_plural = 'Produtos'
        db_table = 'produto'
    
    def __str__(self):
        return (f'{self.nome} | {self.marca} | R$ {str(self.preco)}') 

class Avaliacao(models.Model):
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  objects_id = models.PositiveIntegerField()
  content_object = GenericForeignKey('content_type', 'objects_id')
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  nota = models.IntegerField()
  comentario = models.TextField()
  
  def __str__(self):
    return f'{self.usuario.username} - {self.nota}'
  

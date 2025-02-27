from django.db import models

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
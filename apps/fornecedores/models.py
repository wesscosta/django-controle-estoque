from django.db import models
    
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
    
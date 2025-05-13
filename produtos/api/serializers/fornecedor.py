from rest_framework import serializers
from produtos.models import Fornecedor 

class FornecedorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Fornecedor
    fields = '__all__'

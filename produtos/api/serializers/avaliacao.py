from rest_framework import serializers
from produtos.models import Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Avaliacao
    fields = '__all__'

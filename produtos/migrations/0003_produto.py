# Generated by Django 5.1.6 on 2025-03-12 23:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_fornecedor_alter_categoria_nome'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome do produto')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição do Produto')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço')),
                ('quantidadeEstoque', models.PositiveIntegerField(default=0, verbose_name='Quantidade em Estoque')),
                ('imagem', models.ImageField(blank=True, default='/images/placeholder.png', null=True, upload_to='')),
                ('marca', models.CharField(blank=True, max_length=200, null=True)),
                ('avaliacao', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('criadoEm', models.DateTimeField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='produtos.categoria')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='produtos.fornecedor')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'db_table': 'produto',
            },
        ),
    ]

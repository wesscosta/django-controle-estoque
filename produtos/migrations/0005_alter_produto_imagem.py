# Generated by Django 5.1.6 on 2025-03-27 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_alter_produto_criadoem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='imagens'),
        ),
    ]

# 📦 Django Controle de Estoque  

O **Django Controle de Estoque** é um sistema completo para gerenciar produtos, fornecedores, compras e vendas. Desenvolvido com Django, ele oferece uma solução eficiente para o controle de estoque de pequenas e médias empresas, garantindo um fluxo de gestão organizado e otimizado.  

## ✨ Recursos  
- 📊 Dashboard para visualizar o status do estoque  
- 🏷️ Cadastro e gerenciamento de produtos, fornecedores e clientes  
- 🔄 Controle de entradas e saídas de estoque  
- 📜 Registro de compras e vendas com histórico detalhado  
- ⚡ Interface intuitiva e de fácil utilização  

## 🚀 Como Usar  
1. Clone este repositório:  
   ```bash
   git clone https://github.com/wesscosta/django-controle-estoque.git
   ```  
2. Instale as dependências e configure o ambiente Django  
3. Execute as migrações e inicie o servidor  
4. Acesse o painel e comece a gerenciar seu estoque de forma eficiente!  

---
---

## Descrição: Processo para criação de um projeto de controle de estoque contendo  produtos, fornecedores, categorias e movimentação de estoque

## Pre-requisitos
- VSCODE
- Python 3.8 ou superior

### Steps para criação de um projeto
01. Criação do repositorio
> mkdir nome_da_pasta

02. Acessar o Repositorio
> cd nome_da_pasta

03. Criar o ambiente virtual
> python -m venv venv

04. Acessar o ambiente virtual
- windows: 
> venv\Scripts\activate
- linux ou mac:
> source venv/bin/activate 

05. Instalar os pacotes (django,...)
- Instalando um pacote especifico
> pip install django
- Instalando uma lista de pacotes:
> pip install -r requeriments.txt

06. criação do projeto 
> django-admin startproject nome_projeto .

07. criação do app
> django-admin startapp nome_app

08. Criação do model.py[nome_app/models.py] e configuração  em INSTALLED_APPS no arquivo settings.py[nome_projeto/settings.py]

09. Realizar as migrações  no banco de dados
- Faz as migrações dos models
> python manage.py makemigrations
- Aplica as migrações no banco de dados  
> python manage.pt migrate

10. Criação do Super Usuario
> python manage.py  createsuperuser

11. startar o servidor de desenvolvimento
> python manage.py runserver

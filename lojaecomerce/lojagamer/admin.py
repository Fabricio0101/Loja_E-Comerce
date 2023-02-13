from django.contrib import admin
from.models import *


admin.site.register([Cliente,Categoria,Produto,Carrinho,Carrinhoproduto,Pedido_order])
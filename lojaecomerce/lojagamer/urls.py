from django.urls import path
from.views import *


app_name = "lojagamer"
urlpatterns = [
    path("",HomeView.as_view(), name="home"),
    path("sobre/",SobreView.as_view(), name="sobre"),
    path("contato/",ContatoView.as_view(), name="contato"),
    path("todos-produtos/",TodosProdutosView.as_view(), name="Todosprodutos"),
    path("produto/<slug:slug>/",ProdutoDetalheView.as_view(), name="produtodetalhe"),
    path("addcarrinho-<int:pro_id>/",AddCarrinhoView.as_view(), name="addcarrinho"),
    path("meucarrinho/",MeuCarrinhoView.as_view(), name="meucarrinho"),
    path("manipular-carrinho/-<int:cp_id>/",ManipularCarrinhoView.as_view(), name="manipularcarrinho"),
    ##path("limparcarrinho/",LimparCarrinhoView.as_view(), name="limparcarrinho") #url dando erro
    ##path("registrar/-<int:cp_id>/",ClienteRegistrarView.as_view(), name="clienteregistrar"),
]
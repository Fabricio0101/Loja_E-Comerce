from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, CreateView
from.models import *

class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produto_list']= Produto.objects.all().order_by("-id")
        return context

class TodosProdutosView(TemplateView):
    template_name = "todospodutos.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todoscategorias']= Categoria.objects.all()
        return context
    
class ProdutoDetalheView(TemplateView):
    template_name = "produtodetalhe.html"
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = self.kwargs['slug']
        produto = Produto.objects.get(slug=url_slug)
        context['produto']= produto
        return context

class AddCarrinhoView(TemplateView):
    template_name = "addcarrinho.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        produto_id = self.kwargs['pro_id']
        produto_obj = Produto.objects.get(id=produto_id)
        Carrinho_id = self.request.session.get("Carrinho_id",None)
        if Carrinho_id:
            carro_obj = Carrinho.objects.get(id=Carrinho_id)
            produto_no_carrinho = carro_obj.carrinhoproduto_set.filter(produto=produto_obj)
            if produto_no_carrinho.exists():
                carroproduto = produto_no_carrinho.last()
                carroproduto.quantidade += 1
                carroproduto.subtotal += produto_obj.venda
                carroproduto.save()
                carro_obj.total += produto_obj.venda
                carro_obj.save()

            else:
                carroproduto = Carrinhoproduto.objects.create(carro = carro_obj,produto = produto_obj,avaliacao = produto_obj.venda,quantidade = 1,subtotal = produto_obj.venda)
                carro_obj.total += produto_obj.venda
                carro_obj.save()
        else:
            carro_obj = Carrinho.objects.create(total=0)
            self.request.session['Carrinho_id']=carro_obj.id
            carroproduto = Carrinhoproduto.objects.create(carro = carro_obj,produto = produto_obj,avaliacao = produto_obj.venda,quantidade = 1,subtotal = produto_obj.venda)
            carro_obj.total += produto_obj.venda
            carro_obj.save()
        return context

class ManipularCarrinhoView(View):
    def get(self,request,*args, **kwargs):
        cp_id = self.kwargs["cp_id"]
        acao = request.GET.get("acao")
        cp_obj = Carrinhoproduto.objects.get(id=cp_id)
        carrinho_obj = cp_obj.carro

        if acao == "inc":
            cp_obj.quantidade += 1
            cp_obj.subtotal += cp_obj.avaliacao
            cp_obj.save()
            carrinho_obj.total += cp_obj.avaliacao
            carrinho_obj.save()
        elif acao == "dcr":
            cp_obj.quantidade -= 1
            cp_obj.subtotal -= cp_obj.avaliacao
            cp_obj.save()
            carrinho_obj.total -= cp_obj.avaliacao
            carrinho_obj.save()
            if cp_obj.quantidade == 0:
                cp_obj.delete()
        elif acao == "rmv":
            carrinho_obj.total -= cp_obj.subtotal
            carrinho_obj.save()
            cp_obj.delete()
        else:
            pass
        return redirect("lojagamer:meucarrinho")

#class LimparCarrinhoView(View): # Classe Dando Erro
#    def get(self,request,*args, **kwargs):
#        Carrinho_id = request.session.get("Carrinho_id",None)
#        if Carrinho_id:
#            carrinho = Carrinho.objects.get(id=Carrinho_id)
#            carrinho.carrinhoproduto_set.all().delete
#            carrinho.total = 0
#            carrinho.save()
#        return redirect("lojagamer:meucarrinho")

class MeuCarrinhoView(TemplateView): 
    template_name = "meucarrinho.html"
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Carrinho_id = self.request.session.get("Carrinho_id",None)
        if Carrinho_id:
            carrinho = Carrinho.objects.get(id=Carrinho_id)
        else:
            carrinho = None
        context['carrinho'] = carrinho
        return context


#class ClienteRegistrarView(CreateView): # função cadastrar usuário incompleto (não deu tempo)
#    template_name = "clienteregistrar.html"
#    form_class = ClienteRegistrarForm
#        
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
 



class SobreView(TemplateView):
    template_name = "sobre.html"


class ContatoView(TemplateView):
    template_name = "contato.html"



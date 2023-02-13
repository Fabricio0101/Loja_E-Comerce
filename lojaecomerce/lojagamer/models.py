from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200,null=True,blank=True)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.titulo
    

class Produto(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="produtos")
    preco_mercado = models.PositiveBigIntegerField()
    venda = models.PositiveBigIntegerField()
    descricao = models.TextField()
    garantia = models.CharField(max_length=300, null=True,blank=True)
    devolucao = models.CharField(max_length=300,null=True,blank=True)
    visualizacao = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.titulo
    
class Carrinho(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.SET_NULL,null=True,blank=True)
    total = models.PositiveBigIntegerField(default=1)
    criado_em = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return "Carrinho:" + str(self.id)

class Carrinhoproduto(models.Model):
    carro = models.ForeignKey(Carrinho,on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
    avaliacao = models.PositiveBigIntegerField()
    quantidade = models.PositiveBigIntegerField()
    subtotal = models.PositiveBigIntegerField()


    def __str__(self):
        return "Carrinho:" +str(self.carro.id)+ "Carrinhoproduto:" + str(self.id)

PEDIDO_STATUS=(
    ("Pedido Recebido","Pedido Recebido"),
    ("Pedido Processado","Pedido Processado"),
    ("Pedido a Caminho","Pedido a Caminho"),
    ("Pedido Completo","Pedido Completo"),
    ("Pedido Cancelado","Pedido Cancelado"),
)
    
class Pedido_order(models.Model):
    carro = models.OneToOneField(Carrinho,on_delete=models.CASCADE)
    ordenardo_por = models.CharField(max_length=200)
    endereco_envio = models.CharField(max_length=200)
    telefone = models.CharField(max_length=10)
    email = models.EmailField(null=True,blank=True)
    subtotal = models.CharField(max_length=200)
    desconto = models.PositiveBigIntegerField()
    total =  models.PositiveBigIntegerField()
    pedido_status = models.CharField(max_length=50,choices=PEDIDO_STATUS)
    criacao_pedido = models.DateField(auto_now_add=True)


    def __str__(self):
        return "Pedido_order:" + str(self.id)
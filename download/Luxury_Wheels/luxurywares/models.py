from django.db import models



# Modelos de Cliente / Client Model
class Cliente(models.Model):
    CATEGORIA_CHOICES =[
    ('Gold', 'Gold - 600€'),
    ('Silver', 'Silver - 250€'),
    ('Econômico', 'Econômico - 50€'),
]



    nome = models.CharField(max_length=100)         # Name
    email = models.EmailField(unique=True)          # Email
    telefone = models.CharField(max_length=20)      # Phone
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='ECONOMICO')      # Categoria fixa
    
    def __str__(self):
        return f"{self.nome} ({self.categoria})"



# Modelos de Veículos / Vehicle Model
class Veiculo(models.Model):
    marca = models.CharField(max_length=50)         # Brand
    modelo = models.CharField(max_length=50)        # Model
    ano = models.IntegerField()                     # Year   
    placa = models.CharField(max_length=10, unique=True)  # Placa
    disponivel = models.BooleanField(default=True)        # Available
    
    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.placa}"



# Modelos de Formas de Pagamento  / Payment Method Model
class FormaPagamento(models.Model):
    OPÇÕES = [
        ('PIX', 'Pix'),
        ('DINHEIRO', 'Dinheiro'),
        ('CARTAO', 'Cartão de Crédito'),
    ]
    descricao =models.CharField(max_length=50, choices=OPÇÕES, unique=True)      # Description
    
    def __str__(self):
        return self.descricao



# Modelo de Reserva / Reservation Model
class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)      # Client
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)      # Vehicle
    data_inicio = models.DateField()        # Start Date
    data_fim = models.DateField()           # End Date
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.SET_NULL, null=True)   # Payment
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)      # Total Value
    
    # Dicionário de valores por categoria
    VALOR_CATEGORIA = {
        'Gold': 600,
        'Silver': 250,
        'Econômico': 50,
    }
    

    # Sobrescrevendo o save() para calcular o valor total
    def save(self, *args,**kwargs):
        # Calcular a quantidade de dias da reserva
        dias = (self.data_fim - self.data_inicio).days + 1 # incluir o dia inicial
        
        # Obtém o valor diário da categoria do cliente
        # Remove o valor monetário da string, se estiver no formato "Gold - 600€"
        categoria_nome = self.cliente.categoria.split(' ')[0]
        valor_diario = self.VALOR_CATEGORIA.get(categoria_nome, 0)
        
        # Calcular o valor total
        self.valor_total = dias * valor_diario
        
        super().save(*args, **kwargs)



    def __str__(self):
        return f"Reserva de {self.cliente.nome} - {self.veiculo.modelo}"
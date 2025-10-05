from django.contrib import admin
from .models import Cliente, Veiculo, FormaPagamento, Reserva


# Lista fixa de formas de pagamento
FORMA_DE_PAGAMENTO_FIXA = ['PIX', 'Dinheiro', 'Cartão de Crédito']

# Admin para Cliente
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'categoria')  # Mostra categoria
    search_fields = ('nome', 'email')
    list_filter = ('categoria',)  # Filtro lateral por categoria
    ordering = ('nome',)


# Admin para Veículo
@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'ano', 'placa', 'disponivel')
    list_filter = ('disponivel', 'marca')           # Filtro lateral
    search_fields = ('marca', 'modelo', 'placa')
    ordering = ('marca', 'modelo')


# Admin para Forma de Pagamento com lista fixa
@admin.register(FormaPagamento)
class FormaPagamentoAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    ordering = ('descricao',)


# Bloqueio a adição manual e força a lista fixa
def has_add_permission(self, request):
    return False

def get_queryset(self, request):
    qs = super().get_queryset(request)
    # Garante que só aparecem os três items fixos
    return qs.filter(descricao_in=FORMA_DE_PAGAMENTO_FIXA)


# Admin para Reserva
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'veiculo', 'data_inicio', 'data_fim', 'forma_pagamento', 'valor_total')
    list_filter = ('data_inicio', 'data_fim', 'forma_pagamento')
    search_fields = ('cliente__nome', 'veiculo__modelo')
    ordering = ('data_inicio',)
    
    # Tornar o campo valor total somente leitura no admin
    readonly_fields = ('valor_total',)

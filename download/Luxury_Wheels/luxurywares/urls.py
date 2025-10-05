"""
URL configuration for luxurywares project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from luxurywares import views  # IMPORTANTE: se este urls.py estiver DENTRO do app, use "from . import views"

urlpatterns = [
    path('admin/', admin.site.urls),

    # página principal (opcional)
    path('', views.home, name='home'),

    # rotas de reserva (ACRESCENTADAS)
    path('criar_reserva/', views.criar_reserva, name='criar_reserva'),
    path('listar_reserva/', views.listar_reserva, name='listar_reserva'),
    path('reserva/<int:id>/editar/', views.editar_reserva, name='editar_reserva'),
    path('reserva/<int:id>/excluir/', views.excluir_reserva, name='editar_reserva'),
    
        # rotas de clientes
    path('listar_clientes/', views.listar_clientes, name='listar_clientes'),
    path('cliente/<int:id>/editar/', views.editar_cliente, name='editar_cliente'),
    path('cliente/<int:id>/excluir/', views.excluir_cliente, name='confirmar_excluir_cliente'),
    path('criar_cliente/', views.criar_cliente, name='criar_cliente'),

    # rotas de veículos
    path('listar_veiculos/', views.listar_veiculos, name='listar_veiculos'),
    path('veiculo/<int:id>/editar/', views.editar_veiculo, name='editar_veiculo'),
    path('veiculo/<int:id>/excluir/', views.excluir_veiculo, name='confirmar_excluir_veiculo'),
    path('criar_veiculo/', views.criar_veiculo, name='criar_veiculo'),

]

from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva
from .forms import ReservaForm

# Home simples (página inicial)
def home(request):
    return redirect('listar_reserva')  # redireciona para lista de reservas

# Criar reserva
def criar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()  # o save() do model calcula valor_total automaticamente
            return redirect('listar_reserva')
    else:
        form = ReservaForm()
    return render(request, 'cliente/criar_reserva.html', {'form': form})

# Listar reservas
def listar_reserva(request):
    reservas = Reserva.objects.all().order_by('-data_inicio')
    return render(request, 'cliente/listar_reserva.html', {'reservas': reservas})

# Editar reserva
def editar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('listar_reserva')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'cliente/criar_reserva.html', {'form': form, 'editar': True})

# Excluir reserva
def excluir_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        reserva.delete()
        return redirect('listar_reserva')
    return render(request, 'cliente/confirmar_excluir.html', {'reserva': reserva})

# =============================
# CLIENTES
# =============================
from .models import Cliente

def listar_clientes(request):
    clientes = Cliente.objects.all().order_by('nome')
    return render(request, 'cliente/listar_clientes.html', {'clientes': clientes})

def criar_cliente(request):
    from .forms import ClienteForm
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'cliente/criar_cliente.html', {'form': form})

def editar_cliente(request, id):
    from .forms import ClienteForm
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente/criar_cliente.html', {'form': form, 'editar': True})

def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'cliente/confirmar_excluir.html', {'cliente': cliente})


# =============================
# VEÍCULOS
# =============================
from .models import Veiculo

def listar_veiculos(request):
    veiculos = Veiculo.objects.all().order_by('modelo')
    return render(request, 'cliente/listar_veiculos.html', {'veiculos': veiculos})

def criar_veiculo(request):
    from .forms import VeiculoForm
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_veiculos')
    else:
        form = VeiculoForm()
    return render(request, 'cliente/criar_veiculo.html', {'form': form})

def editar_veiculo(request, id):
    from .forms import VeiculoForm
    veiculo = get_object_or_404(Veiculo, id=id)
    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            return redirect('listar_veiculos')
    else:
        form = VeiculoForm(instance=veiculo)
    return render(request, 'cliente/criar_veiculo.html', {'form': form, 'editar': True})

def excluir_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('listar_veiculos')
    return render(request, 'cliente/confirmar_excluir.html', {'veiculo': veiculo})

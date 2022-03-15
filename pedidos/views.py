from typing import List
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from pedidos.models import Cliente, Pedidos
from .forms import ComidaForms, PedidoFormset


def comida(request):
    data = {
        'form': ComidaForms()
        }
    if request.method == 'POST':
        formulario = ComidaForms(data=request.POST)

        if formulario.is_valid():
            formulario.save()
        else:
            data["form"] = formulario

    return render(request, 
        'pedidos/comida_add.html',
        context=data )
"""fields = ('nombre_cliente', 'direccion', 'ciduad', 'telefono', 'articulo', 'fecha')"""
class ClienteListView(ListView):
    model = Cliente

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre_cliente', 'direccion', 'ciduad', 'telefono']

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        if self.request.POST:
            data['pedido'] = PedidoFormset(self.request.POST)
        else:
            data['pedido'] = PedidoFormset()
        
        return data

    def form_valid(self, form):
        ctx = self.get_context_data()
        cliente = ctx['pedido']
        self.object = form.save()
        if cliente.is_valid():
            cliente.instance = self.object
            cliente.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("cliente")

    
"""def pedidos(request):
    data = {
        'form': 
        }
    if request.method == 'POST':
        formulario = ComidaForms(data=request.POST)

        if formulario.is_valid():
            formulario.save()
        else:
            data["form"] = formulario

    return render(request, 
        'pedidos/comida_add.html',
        context=data )"""
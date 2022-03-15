from django import forms
from django.forms import fields
from django.forms.models import inlineformset_factory
from .models import Comida, Pedidos, Cliente

class ComidaForms(forms.ModelForm):

    class Meta: 
        model = Comida
        fields = ['nombre', 'valor']

PedidoFormset = inlineformset_factory(Cliente, Pedidos, fields=['articulo', 'fecha'], max_num=2)
""" class PedidosForm(forms.ModelForm):

    class Meta:
        model = Pedidos
        fields = [Cliente(), 'articulo', 'fecha'] """
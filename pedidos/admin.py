from django.contrib import admin

from pedidos.models import Cliente, Comida, Pedidos

admin.site.register(Comida)

admin.site.register(Cliente)

admin.site.register(Pedidos)
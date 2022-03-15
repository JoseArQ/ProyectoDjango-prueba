from django.db import models

"""
1- Se debe crear un formulario donde 
se puedan crear los articulos (comida) que 
seran vendidos, debe contener, el nombre y el valor.
"""
class Comida(models.Model):
    nombre = models.CharField(max_length=50)
    valor = models.FloatField(verbose_name='costo del producto')

    def __str__(self):
        return f'{self.nombre} ${self.valor}'
"""
2- Se debe crear un formulario de pedidos de un restaurante, 
los campos que debe tener son los siguientes: Nombre del cliente, 
fecha y hora del pedido, articulo (debe cargar los articulos registrados
 en el formulario anterior), cantidad, valor total, dirección, ciudad, telefono del cliente.
"""
class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    ciduad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)


class Pedidos(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    articulo = models.ForeignKey('Comida', on_delete=models.CASCADE)
    fecha =  models.DateField(null=True, blank=True)

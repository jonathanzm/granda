from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import Cliente
from .models import Producto

class AdminCliente(admin.ModelAdmin):
	list_display = ["nombres","apellidos","cedula_identidad","direccion","telefono","estado"]
	search_fields = ["nombres"]
	class Meta:
		model = Cliente

admin.site.register(Cliente,AdminCliente)

class AdminProducto(admin.ModelAdmin):
	list_display = ["nombre","precio","medidas","tipo_producto"]
	fields= ("nombre",("precio","medidas"),"tipo_producto")
	search_fields= ["nombre"]
	class Meta:
		model = Producto


admin.site.register(Producto,AdminProducto)
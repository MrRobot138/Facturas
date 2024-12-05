from django.contrib import admin

from .models import Factura, ResumenDeCuenta, Estudiante, Institucion

admin.site.register(Factura)
admin.site.register(ResumenDeCuenta)
admin.site.register(Estudiante)
admin.site.register(Institucion)
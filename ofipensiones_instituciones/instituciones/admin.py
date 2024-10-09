from django.contrib import admin

from .models import ReciboDePago, ResumenDeCuenta, Estudiante, Institucion

admin.site.register(ReciboDePago)
admin.site.register(ResumenDeCuenta)
admin.site.register(Estudiante)
admin.site.register(Institucion)
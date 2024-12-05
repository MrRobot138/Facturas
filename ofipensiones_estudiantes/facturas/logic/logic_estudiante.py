from ..models import Factura
from django.shortcuts import get_object_or_404

def get_facturas(id_estudiante):
    facturas = Factura.objects.filter(resumenDeCuenta__estudiante_id=id_estudiante)
    data = [{
        'idFactura': factura.idFactura,
        'fechaPago': factura.fechaPago,
        'valorACancelar': factura.valorACancelar,
        'estadoCuenta': factura.resumenDeCuenta.estado
    } for factura in facturas] 
    return (data)

def get_all_facturas():
    facturas = Factura.objects.all()
    data = {}

    for factura in facturas:
        estudiante_id = factura.resumenDeCuenta.estudiante.codigo
        if estudiante_id not in data:
            data[estudiante_id] = []
        data[estudiante_id].append({
            'idFactura': factura.idFactura,
            'fechaPago': factura.fechaPago,
            'valorACancelar': factura.valorvalorACancelar,
            'estadoCuenta': factura.resumenDeCuenta.estado
        })
    return (data)


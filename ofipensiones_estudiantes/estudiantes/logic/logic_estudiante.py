from ..models import ReciboDePago, Estudiante
from django.shortcuts import get_object_or_404

def get_recibos(id_estudiante):
    recibos = ReciboDePago.objects.filter(resumenDeCuenta__estudiante_id=id_estudiante)
    data = [{
        'idRecibo': recibo.idRecibo,
        'fechaPago': recibo.fechaPago,
        'valorCancelado': recibo.valorCancelado,
        'estadoCuenta': recibo.resumenDeCuenta.estado
    } for recibo in recibos] 
    return (data)

def get_all_recibos():
    recibos = ReciboDePago.objects.all()
    data = {}

    for recibo in recibos:
        estudiante_id = recibo.resumenDeCuenta.estudiante.codigo
        if estudiante_id not in data:
            data[estudiante_id] = []
        data[estudiante_id].append({
            'idRecibo': recibo.idRecibo,
            'fechaPago': recibo.fechaPago,
            'valorCancelado': recibo.valorCancelado,
            'estadoCuenta': recibo.resumenDeCuenta.estado
        })
    return (data)

def get_estudiantes():
    estudiantes = Estudiante.objects.all().values('codigo', 'nombre', 'grado', 'institucion__nombre')
    return (estudiantes)

def get_estudiante(id_estudiante):
    estudiante = get_object_or_404(Estudiante, id=id_estudiante)
    data = {
        'codigo': estudiante.codigo,
        'nombre': estudiante.nombre,
        'grado': estudiante.grado,
        'institucion': estudiante.institucion.nombre if estudiante.institucion else None
    }
    return (data)
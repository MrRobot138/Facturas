from ..models import ReciboDePago

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
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
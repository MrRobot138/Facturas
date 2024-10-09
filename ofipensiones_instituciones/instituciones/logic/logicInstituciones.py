from ..models import ReciboDePago
from ..models import ResumenDeCuenta


def get_recibos_de_pagos():
    pagos = ReciboDePago.objects.all()
    return pagos

def create_recibos_de_pagos(form):
    pago = form.save()
    pago.save()
    return ()

def create_recibos_de_pagos_object(fecha, valor, tipo, cc, entidad, idResumenDeCuenta):
    pago = ReciboDePago()
    pago.valorCancelado = valor
    pago.tipoDePago = tipo
    pago.fechaPago = fecha
    pago.resumenDeCuenta = idResumenDeCuenta
    pago.ccDelResponsable = cc
    pago.entidadBancaria = entidad
    pago.save()
    return()

def create_resumen_de_cuenta_object(estado, saldo, saldoPend, fechaUltimoPago):
    resumen = ResumenDeCuenta()
    resumen.estado = estado
    resumen.saldo = saldo
    resumen.saldoPendiente = saldoPend
    resumen.fechaUltimaPago = fechaUltimoPago
    resumen.save()
    return()

def get_recibos(id_estudiante):
    recibos = ReciboDePago.objects.filter(resumenDeCuenta__estudiante_id=id_estudiante)
    data = [{
        'idRecibo': recibo.idRecibo,
        'fechaPago': recibo.fechaPago,
        'valorCancelado': recibo.valorCancelado,
        'estadoCuenta': recibo.resumenDeCuenta.estado
    } for recibo in recibos] 
    return (data)
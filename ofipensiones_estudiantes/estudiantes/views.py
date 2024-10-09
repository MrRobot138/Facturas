#from django.shortcuts import render
from django.http import JsonResponse
from .logic.logic_estudiante import get_recibos

def consulta_estado_pago(request, id_estudiante):
    data = get_recibos(id_estudiante)
    return JsonResponse({'data': data})

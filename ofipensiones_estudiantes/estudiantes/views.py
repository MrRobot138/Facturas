#from django.shortcuts import render
from django.http import JsonResponse
from .logic.logic_estudiante import get_recibos, get_all_recibos

def consulta_estado_pago(request, id_estudiante):
    data = get_recibos(id_estudiante)
    return JsonResponse({'data': data})

def consulta_all_estado_pago(request):
    data = get_all_recibos()
    return JsonResponse({'estudiantes': data})

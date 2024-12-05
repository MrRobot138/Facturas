#from django.shortcuts import render
from django.http import JsonResponse
from .logic.logic_estudiante import get_all_facturas, get_facturas
from django.http import HttpResponse

def consulta_factura(request, id_estudiante):
    data = get_facturas(id_estudiante)
    return JsonResponse({'data': data})

def consulta_all_facturas(request):
    data = get_all_facturas()
    return JsonResponse({'estudiantes': data})


def healthCheck(request):  # Nueva función añadida para Health Check
    return HttpResponse('ok')

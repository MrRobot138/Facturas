#from django.shortcuts import render
from django.http import JsonResponse
from .logic.logic_estudiante import get_recibos, get_all_recibos, get_estudiantes, get_estudiante
from django.http import HttpResponse

def consulta_estado_pago(request, id_estudiante):
    data = get_recibos(id_estudiante)
    return JsonResponse({'data': data})

def consulta_all_estado_pago(request):
    data = get_all_recibos()
    return JsonResponse({'estudiantes': data})

def consulta_estudiantes(request):
    data = get_estudiantes()
    return JsonResponse({'estudiantes': list(data)})

def consulta_estudiante_por_id(request, id_estudiante):
    data = get_estudiante(id_estudiante)
    return JsonResponse({'estudiante': data})

def healthCheck(request):  # Nueva función añadida para Health Check
    return HttpResponse('ok')

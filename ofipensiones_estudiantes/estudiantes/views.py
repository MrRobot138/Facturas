#from django.shortcuts import render
from django.http import JsonResponse
from .logic.logic_estudiante import get_recibos, get_all_recibos, get_estudiantes, get_estudiante
from django.http import HttpResponse
from django.core.cache import cache
from ofipensiones_estudiantes.auth0backend import getRole
from django.contrib.auth.decorators import login_required

def consulta_estado_pago(request, id_estudiante):
    data = get_recibos(id_estudiante)
    return JsonResponse({'data': data})

def consulta_estados_pagos(request):
    data = get_all_recibos()
    return JsonResponse({'estudiantes': data})



@login_required
def consulta_all_estado_pago(request):
    role = getRole(request)
    if role == "Contador":
        data = get_all_recibos()
        return JsonResponse({'estudiantes': data})
    else:
        return JsonResponse({'message': 'Unauthorized'}, status=401)


@login_required
def consulta_estudiantes(request):
    role = getRole(request)
    if role == "Administrator":
        data = cache.get('my_data_key')
        if not data:
            data = get_estudiantes() 
            cache.set('my_data_key', data, timeout=1)
        return JsonResponse({'estudiantes': list(data)})
    else:
        return JsonResponse({'message': 'Unauthorized'}, status=401)

def consulta_estudiante_por_id(request, id_estudiante):
    data = get_estudiante(id_estudiante)
    return JsonResponse({'estudiante': data})

def healthCheck(request):  # Nueva función añadida para Health Check
    return HttpResponse('ok')

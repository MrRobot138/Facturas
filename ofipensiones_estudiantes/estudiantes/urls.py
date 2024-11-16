from django.urls import path
from . import views

urlpatterns = [
    path('consulta/<int:id_estudiante>/', views.consulta_estado_pago, name='consulta_estado_pago'),
    path('consulta-todos/', views.consulta_all_estado_pago, name='consulta_all_estado_pago'),
    path('health-check/', views.healthCheck),  # Nueva línea añadida para Health Check     
    path('consulta-estudiante/', views.consulta_estudiantes, name='consulta_estudiantes'),
    path('consulta_estados_pagos/', views.consulta_estados_pagos, name='consulta_estados_pagos'),
    path('consulta-estudiante/<int:id_estudiante>', views.consulta_estudiante_por_id, name='consulta_estudiante_por_id')
]


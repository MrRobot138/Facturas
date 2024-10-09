from django.urls import path
from . import views

urlpatterns = [
    path('consulta/<int:id_estudiante>/', views.consulta_estado_pago, name='consulta_estado_pago'),
    path('health-check/', views.healthCheck),  # Nueva línea añadida para Health Check     
]

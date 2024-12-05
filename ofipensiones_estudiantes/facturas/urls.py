from django.urls import path
from . import views

urlpatterns = [
    path('consulta/<int:id_estudiante>/', views.consulta_factura, name='consulta_factura'),
    path('consulta-todos/', views.consulta_all_facturas, name='consulta_all_facturas'),
    path('health-check/', views.healthCheck),  # Nueva línea añadida para Health Check     
]


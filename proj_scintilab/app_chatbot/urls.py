from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PaginaInicialView.as_view(), name='pagina-inicial'),
    path('os/', views.OrdemServicoView.as_view(), name='pagina-os'),
    path('os-ativas/', views.OrdemServicoAtivaView.as_view(), name='pagina-os-ativas'),
]
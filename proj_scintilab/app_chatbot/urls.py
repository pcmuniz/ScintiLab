from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home-page'),
    path('cliente/', views.CustomerPage.as_view(), name='customer-page'),
    path('login-cliente/', views.CustomerLoginPage.as_view(), name='customer-login-page'),
    path('cadastro-cliente/', views.CustomerRegisterPage.as_view(), name='customer-register-page'),
    path('login-funcionario/', views.EmployeeLoginPage.as_view(), name='employee-login-page'),
    path('cadastro-funcionario/', views.EmployeeRegisterPage.as_view(), name='employee-register-page'),
    path('os/', views.OrdemServicoView.as_view(), name='pagina-os'),
    path('os-ativas/', views.OrdemServicoAtivaView.as_view(), name='pagina-os-ativas'),

    # Abaixo são as URL's para teste de funcionalidade focado no backend
    # São provisórias!
    path('cadastro/', views.registration_view, name='cadastro'),
    path('change_order_status/<int:order_id>/', views.ChangeOrderStatus.as_view(), name='change_order_status'),
    path('ordem-servico/<int:order_id>/cancelar/', views.CancelOrder.as_view(), name='cancelar_ordem_servico'),
    path('modal/', views.Modal.as_view(), name='cancelar_ordem_servico'),
    path('teste/', views.Teste.as_view(), name='teste'),
]
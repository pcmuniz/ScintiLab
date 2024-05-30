from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home-page'),
    path('login-cliente/', views.CustomerLoginPage.as_view(), name='customer-login-page'),
    path('cadastro-cliente/', views.CustomerRegisterPage.as_view(), name='customer-register-page'),
    path('login-funcionario/', views.EmployeeLoginPage.as_view(), name='employee-login-page'),
    path('cadastro-funcionario/', views.EmployeeRegisterPage.as_view(), name='employee-register-page'),
    path('os/', views.OrdemServicoView.as_view(), name='pagina-os'),
    path('os-ativas/', views.OrdemServicoAtivaView.as_view(), name='pagina-os-ativas'),
    path('chatbot/', views.ChatbotView.as_view(), name='chatbot'),

]
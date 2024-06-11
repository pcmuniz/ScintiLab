from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home-page'),
    path('login/', auth_views.LoginView.as_view(template_name='app_chatbot/login.html'), name='login'),
    path('lista-os/', login_required(views.ServiceOrderListView.as_view()), name = 'service_order_list'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app_chatbot/logout.html'), name='logout'),
    path('cliente/', views.CustomerPageView.as_view(), name='customer-page'),
    path('abrir-os/', views.ServiceOrderView.as_view(), name='service_order'),
    path('cliente/ordens/', views.CustomerOrders.as_view(), name='customer-orders'),

    # Abaixo são as URL's para teste de funcionalidade focado no backend
    # São provisórias!

    # path('cstatus/', views.ChangeOrderStatus2.as_view(), name='change-order-status'),
    path('cstatus/<int:order_id>/', views.ChangeOrderStatus2.as_view(), name='change-order-status'),

    path('change_order_status/<int:order_id>/', views.ChangeOrderStatus.as_view(), name='change_order_status'),
    # path('ordem-servico/<int:order_id>/cancelar/', views.CancelOrder.as_view(), name='cancelar_ordem_servico'),
    path('cancel-order-c/<int:order_id>/', views.CancelOrderClient.as_view(), name='cancel_order_client'),
    path('cancel-order-e/<int:order_id>/', views.CancelOrderEmployee.as_view(), name='cancel_order_employee'),
    path('modal/', views.Modal.as_view(), name='cancelar_ordem_servico'),
]
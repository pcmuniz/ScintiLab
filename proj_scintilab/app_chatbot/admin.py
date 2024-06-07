from django.contrib import admin
from .models import ClientData, BuyerData, PurchaseData, EquipmentData, ServiceOrder

admin.site.register(ClientData)
admin.site.register(BuyerData)
admin.site.register(PurchaseData)
admin.site.register(EquipmentData)
admin.site.register(ServiceOrder)
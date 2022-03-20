from django.contrib import admin
from .import models


@admin.register(models.Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('client', 'date_created', 'support_contact', 'sales_contact')
    list_filter = ['date_created']
    search_fields = ('client', 'date_created', 'support_contact', 'sales_contact')

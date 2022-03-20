from django.contrib import admin
from . import models


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('client', 'date', 'support_contact', 'sales_contact')
    search_fields = ('client', 'date', 'support_contact', 'sales_contact')


admin.site.register(models.EventStatu)

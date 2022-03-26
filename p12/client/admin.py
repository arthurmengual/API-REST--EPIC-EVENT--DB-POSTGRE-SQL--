from django.contrib import admin
from . import models


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("status", "first_name", "last_name")
    list_filter = ["status"]
    search_fields = ("status", "last_name", "support_contact", "sales_contact")

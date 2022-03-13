from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.Client)
admin.site.register(models.Contract)
admin.site.register(models.Event)
admin.site.register(models.EventStatus)
from django.db import models
from user.models import User
from client.models import Client
from contract.models import Contract


class EventStatu(models.Model):
    CHOICE = (("in process", "in process"), ("finished", "finished"))

    status = models.CharField(choices=CHOICE, max_length=20)

    def __str__(self):
        return self.status


class Event(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    sales_contact = models.ForeignKey(
        User,
        limit_choices_to={"role": "sales"},
        on_delete=models.DO_NOTHING,
        related_name="event_sales_contact",
        null=True,
    )
    support_contact = models.ForeignKey(
        User,
        limit_choices_to={"role": "support"},
        on_delete=models.DO_NOTHING,
        related_name="event_support_contact",
        null=True,
    )
    event_status = models.ForeignKey(EventStatu, on_delete=models.DO_NOTHING)
    attendees = models.IntegerField()
    date = models.DateField()
    notes = models.CharField(max_length=100)
    contract = models.OneToOneField(Contract, on_delete=models.DO_NOTHING, null=True, blank=False)

    def __str__(self):
        return f"event of {self.client.last_name}"

from django.db import models
from user.models import User
from client.models import Client


class Contract(models.Model):
    STATUS_CHOICE = (("signed", "signed"), ("not signed", "not signed"))

    sales_contact = models.ForeignKey(
        User,
        limit_choices_to={"role": "sales"},
        on_delete=models.DO_NOTHING,
        related_name="contract_sales_contact",
    )
    support_contact = models.ForeignKey(
        User,
        limit_choices_to={"role": "support"},
        on_delete=models.DO_NOTHING,
        related_name="contract_support_contact",
        null=True,
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICE, max_length=20)
    amount = models.IntegerField()
    payment_due = models.DateField()

    def __str__(self):
        return self.client.last_name

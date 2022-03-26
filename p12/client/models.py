from django.db import models
from user.models import User


class Client(models.Model):
    STATUS_CHOICE = (("potential", "potential"), ("existing", "existing"))

    status = models.CharField(choices=STATUS_CHOICE, max_length=10, default="potential")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    compagny = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    sales_contact = models.ForeignKey(
        User,
        limit_choices_to={"role": "sales"},
        on_delete=models.DO_NOTHING,
        blank=True,
        related_name="client_sales_contact",
    )
    support_contact = models.ForeignKey(
        User,
        limit_choices_to={"role": "support"},
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="client_support_contact",
    )

    def __str__(self):
        return self.last_name

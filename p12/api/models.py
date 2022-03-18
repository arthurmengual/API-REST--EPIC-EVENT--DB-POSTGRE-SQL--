from distutils.log import error
from lib2to3.pytree import Base
from multiprocessing.sharedctypes import Value
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, user_name, first_name, password, **other_fields):
        if not email:
            raise ValueError('you must provide an email')

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_superuser') is not True:
            raise ValueError('you must check is_superuser')

        if other_fields.get('is_active') is not True:
            raise ValueError('you must check is_active')

        return self.create_user(email, user_name, first_name, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICE = (("manager", "manager"), ("sales", "sales"), ("support", "support"))

    user_name = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    role = models.CharField(choices=ROLE_CHOICE, default="else", max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = ['user_name']
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_name


class Client(models.Model):
    STATUS_CHOICE = (("potential", "potential"), ("existing", "existing"))

    status = models.CharField(choices=STATUS_CHOICE, max_length=10, default="potential")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    compagny = models.CharField(max_length=50)
    date_created = models.DateField(auto_now=True)
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
        blank=True, null=True,
        related_name="client_support_contact"
    )

    def __str__(self):
        return self.last_name


class Contract(models.Model):
    STATUS_CHOICE = (("signed", "signed"), ("not signed", "not signed"))

    sales_contact = models.ForeignKey(
        User, limit_choices_to={"role": "sales"}, on_delete=models.DO_NOTHING, related_name="contract_sales_contact"
    )
    support_contact = models.ForeignKey(
        User,
        limit_choices_to={"role": "support"},
        on_delete=models.DO_NOTHING,
        related_name="contract_support_contact", null=True
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)
    date_updated = models.DateField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICE, max_length=20)
    amount = models.IntegerField()
    payment_due = models.DateField(auto_now=True)

    def __str__(self):
        return self.client.last_name


class EventStatu(models.Model):
    CHOICE = (("in process", "in process"), ("finished", "finished"))

    status = models.CharField(choices=CHOICE, max_length=20)

    def __str__(self):
        return self.status


class Event(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)
    date_updated = models.DateField(auto_now=True)
    sales_contact = models.ForeignKey(
        User,
        limit_choices_to={"role": "sales"},
        on_delete=models.DO_NOTHING,
        related_name="event_sales_contact", null=True
    )
    support_contact = models.ForeignKey(
        User,
        limit_choices_to={"role": "support"},
        on_delete=models.DO_NOTHING,
        related_name="event_support_contact", null=True
    )
    event_status = models.ForeignKey(EventStatu, on_delete=models.DO_NOTHING)
    attendees = models.IntegerField()
    date = models.DateField(auto_now=True)
    notes = models.CharField(max_length=100)

    def __str__(self):
        return f"event of {self.client.last_name}"

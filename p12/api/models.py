from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICE = (('manager', 'manager'),
                   ('sales', 'sales'), ('support', 'support'))

    role = models.CharField(choices=ROLE_CHOICE, default='else', max_length=20)

    def __str__(self):
        return self.username


class Client(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    compagny = models.CharField(max_length=50)
    date_created = models.DateField(auto_now=True)
    date_updated = models.DateField(auto_now=True)
    sales_contact = models.ForeignKey(
        User, limit_choices_to={'role': 'sales'}, on_delete=models.DO_NOTHING, related_name='sales_contact')

    def __str__(self):
        return self.last_name


class Contract(models.Model):
    STATUS_CHOICE = (('signed', 'signed'), ('not signed', 'not signed'))

    sales_contact = models.ForeignKey(
        User, limit_choices_to={'role': 'sales'}, on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)
    date_updated = models.DateField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICE, max_length=20)
    amount = models.IntegerField()
    payment_due = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class EventStatus(models.Model):
    CHOICE = (('processing', 'processing'), ('finished', 'finished'))

    status = models.CharField(choices=CHOICE, max_length=20)

    def __str__(self):
        return self.status


class Event(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)
    date_updated = models.DateField(auto_now=True)
    support = models.ForeignKey(User, limit_choices_to={
        'role': 'support'}, on_delete=models.DO_NOTHING, related_name='support_contact')
    event_status = models.ForeignKey(EventStatus, on_delete=models.DO_NOTHING)
    attendees = models.IntegerField()
    date = models.DateField(auto_now=True)
    notes = models.CharField(max_length=100)

    def __str__(self):
        return f'event of {self.name}'

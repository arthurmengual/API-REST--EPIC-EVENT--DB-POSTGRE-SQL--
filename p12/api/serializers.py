from multiprocessing.connection import Client
from rest_framework.serializers import ModelSerializer
from api import models


class ClientSerializer(ModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'


class ContractSerializer(ModelSerializer):
    class Meta:
        model = models.Contract
        fields = '__all__'


class EventSerializer(ModelSerializer):
    class Meta:
        model = models.Event
        fields = '__all__'


class EventStatuSerializer(ModelSerializer):
    class Meta:
        model = models.EventStatu
        fields = '__all__'

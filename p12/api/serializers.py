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


class EventStatusSerializer(ModelSerializer):
    class Meta:
        model = models.EventStatus
        fields = '__all__'

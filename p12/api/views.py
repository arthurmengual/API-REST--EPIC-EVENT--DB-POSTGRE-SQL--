from rest_framework.viewsets import ModelViewSet
from api import models
from api import serializers


class UserViewSet(ModelViewSet):

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class ClientViewset(ModelViewSet):

    serializer_class = serializers.ClientSerializer
    queryset = models.Client.objects.all()


class ContractViewset(ModelViewSet):

    serializer_class = serializers.ContractSerializer
    queryset = models.Contract.objects.all()


class EventViewset(ModelViewSet):

    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()


class EventStatusViewset(ModelViewSet):

    serializer_class = serializers.EventStatusSerializer
    queryset = models.EventStatus.objects.all()

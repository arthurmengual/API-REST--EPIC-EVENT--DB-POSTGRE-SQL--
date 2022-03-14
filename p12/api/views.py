from rest_framework.viewsets import ModelViewSet
from api import models
from api import serializers

# virer ce viewset


class UserViewSet(ModelViewSet):

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    http_method_names = ["get", "post", "put", "delete"]


class ClientViewset(ModelViewSet):

    serializer_class = serializers.ClientSerializer
    queryset = models.Client.objects.all()
    http_method_names = ["get", "post", "put", "delete"]


class ContractViewset(ModelViewSet):

    serializer_class = serializers.ContractSerializer
    queryset = models.Contract.objects.all()
    http_method_names = ["get", "post", "put", "delete"]


class EventViewset(ModelViewSet):

    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()
    http_method_names = ["get", "post", "put", "delete"]


class EventStatusViewset(ModelViewSet):

    serializer_class = serializers.EventStatusSerializer
    queryset = models.EventStatus.objects.all()
    http_method_names = ["get", "post", "put", "delete"]

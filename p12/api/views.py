from rest_framework.viewsets import ModelViewSet
from api import models
from api import serializers


# surcharger les vues pour que le mec qui créé un client est devienne son sale contact, le mec qui créé un contrat devient
# son sales contact, pareil pour creer un evenement


class ClientViewset(ModelViewSet):

    serializer_class = serializers.ClientSerializer
    queryset = models.Client.objects.all()
    http_method_names = ["get", "post", "put", "delete"]

    def get_queryset(self):
        sales_contact = self.kwargs.get("sales_contact")
        support_contact = self.kwargs.get("support_contact")
        return models.Client.objects.filter(
            sales_contact=sales_contact
        ) | models.Client.objects.filter(support_contact=support_contact)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class ContractViewset(ModelViewSet):

    serializer_class = serializers.ContractSerializer
    queryset = models.Contract.objects.all()
    http_method_names = ["get", "post", "put", "delete"]

    def get_queryset(self):
        sales_contact = self.kwargs.get("sales_contact")
        support_contact = self.kwargs.get("support_contact")
        return models.Client.objects.filter(
            sales_contact=sales_contact
        ) | models.Client.objects.filter(support_contact=support_contact)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class EventViewset(ModelViewSet):

    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()
    http_method_names = ["get", "post", "put", "delete"]

    def get_queryset(self):
        sales_contact = self.kwargs.get("sales_contact")
        support_contact = self.kwargs.get("support_contact")
        return models.Client.objects.filter(
            sales_contact=sales_contact
        ) | models.Client.objects.filter(support_contact=support_contact)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class EventStatusViewset(ModelViewSet):

    serializer_class = serializers.EventStatusSerializer
    queryset = models.EventStatus.objects.all()
    http_method_names = ["get", "post", "put", "delete"]

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .import serializers, models


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
        request.POST._mutable = True
        request.POST['sales_contact'] = request.user.pk
        request.POST._mutable = False
        return super().create(request, *args, **kwargs)

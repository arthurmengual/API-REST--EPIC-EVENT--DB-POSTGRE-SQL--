from rest_framework.viewsets import ModelViewSet
from .import serializers, models
from django_filters import rest_framework as filters
from .permissions import ContractPermission


class ContractViewset(ModelViewSet):

    serializer_class = serializers.ContractSerializer
    queryset = models.Contract.objects.all()
    http_method_names = ["get", "post", "put", "delete"]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['client__last_name', 'client__email', 'date_created', 'amount']
    permission_classes = [ContractPermission]

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data['sales_contact'] = request.user.pk
        request.POST._mutable = False
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data['sales_contact'] = request.user.pk
        request.POST._mutable = False
        return super().update(request, *args, **kwargs)

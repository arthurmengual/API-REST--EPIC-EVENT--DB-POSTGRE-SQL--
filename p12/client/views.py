from rest_framework.viewsets import ModelViewSet
from . import serializers, models, permissions
from django_filters import rest_framework as filters


class ClientViewset(ModelViewSet):

    serializer_class = serializers.ClientSerializer
    queryset = models.Client.objects.all()
    http_method_names = ["get", "post", "put", "delete"]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('last_name', 'email')
    permission_classes = [permissions.ClientPermission]

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

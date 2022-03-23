from rest_framework.viewsets import ModelViewSet
from . import models, serializers, permissions
from django_filters import rest_framework as filters


class EventViewset(ModelViewSet):

    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()
    http_method_names = ["get", "post", "put", "delete"]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['client__last_name', 'client__email', 'date']
    permission_classes = [permissions.EventPermission]

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


class EventStatusViewset(ModelViewSet):

    serializer_class = serializers.EventStatuSerializer
    queryset = models.EventStatu.objects.all()
    http_method_names = ["get", "post", "put", "delete"]

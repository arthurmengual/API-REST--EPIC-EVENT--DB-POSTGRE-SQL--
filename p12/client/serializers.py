from rest_framework.serializers import ModelSerializer
from . import models


class ClientSerializer(ModelSerializer):
    class Meta:
        model = models.Client
        fields = "__all__"

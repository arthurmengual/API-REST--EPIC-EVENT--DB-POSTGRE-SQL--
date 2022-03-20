from rest_framework.serializers import ModelSerializer
from . import models


class ContractSerializer(ModelSerializer):
    class Meta:
        model = models.Contract
        fields = '__all__'

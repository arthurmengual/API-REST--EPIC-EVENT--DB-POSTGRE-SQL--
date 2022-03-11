from rest_framework.viewsets import ModelViewSet
import models
import serializers


class UserViewSet(ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permissions = []

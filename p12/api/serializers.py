from rest_framework.serializers import ModelSerializer
import models


class UserSerializers(ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', 'email']

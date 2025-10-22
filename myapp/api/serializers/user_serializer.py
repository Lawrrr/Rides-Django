from rest_framework import serializers
from api.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id_user",
            "email",
            "role",
            "first_name",
            "last_name",
            "phone_number"
        ]

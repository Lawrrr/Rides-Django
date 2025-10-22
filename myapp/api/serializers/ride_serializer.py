from rest_framework import serializers
from api.models import Ride
from .user_serializer import UserSerializer

class RideSerializer(serializers.ModelSerializer):
    driver = UserSerializer(source="id_driver", read_only=True)
    rider = UserSerializer(source="id_rider", read_only=True)

    class Meta:
        model = Ride
        fields = "__all__"

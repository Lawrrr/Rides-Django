from rest_framework import serializers
from api.models import RideEvent
from .ride_serializer import RideSerializer

class RideEventSerializer(serializers.ModelSerializer):
    ride = RideSerializer(source="id_ride", read_only=True)

    class Meta:
        model = RideEvent
        fields = "__all__"

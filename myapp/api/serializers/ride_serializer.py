from rest_framework import serializers
from api.models import Ride
from .user_serializer import UserSerializer
from .ride_event_serializer import RideEventSerializer

class RideSerializer(serializers.ModelSerializer):
    driver = UserSerializer(source="id_driver", read_only=True)
    rider = UserSerializer(source="id_rider", read_only=True)
    distance = serializers.FloatField(read_only=True) 
    todays_ride_events = RideEventSerializer(many=True, read_only=True)

    class Meta:
        model = Ride
        fields = "__all__"

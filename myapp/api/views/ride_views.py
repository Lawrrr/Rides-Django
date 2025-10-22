from rest_framework import viewsets
from api.models import Ride
from api.serializers import RideSerializer

class RideViewset(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

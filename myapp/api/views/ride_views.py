from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsAdmin
from api.models import Ride
from api.serializers import RideSerializer

class RideViewset(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

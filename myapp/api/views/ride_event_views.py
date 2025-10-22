from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsAdmin
from api.models import RideEvent
from api.serializers import RideEventSerializer

class RideEventViewset(viewsets.ModelViewSet):
    queryset = RideEvent.objects.all()
    serializer_class = RideEventSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

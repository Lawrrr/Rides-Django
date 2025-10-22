from rest_framework import viewsets
from api.models import RideEvent
from api.serializers import RideEventSerializer

class RideEventViewset(viewsets.ModelViewSet):
    queryset = RideEvent.objects.all()
    serializer_class = RideEventSerializer

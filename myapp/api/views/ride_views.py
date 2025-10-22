from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsAdmin
from api.models import Ride
from api.serializers import RideSerializer

class RideViewset(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    @action(detail=False, methods=['get'])
    def rider_email(self, request):
        email = request.query_params.get('email')
        
        if not email:
            return Response(
                {"error": "Please provide email as query parameter"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        rides = Ride.objects.filter(id_rider__email=email)
        serializer = RideSerializer(rides, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def ride_status(self, request):
        statusParam = request.query_params.get('status')
        
        if not status:
            return Response(
                {"error": "Please provide status as query parameter"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        rides = Ride.objects.filter(status=statusParam)
        serializer = RideSerializer(rides, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

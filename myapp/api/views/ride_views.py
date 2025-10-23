from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

# API app
from api.permissions import IsAdmin
from api.models import Ride
from api.serializers import RideSerializer

# Helper defs
from api.helpers import annotate_distance, filter_nearby

class RideViewset(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def list(self, request, *args, **kwargs):
        """
        Default sorting is pickup_time when there is no sort query param
        url sample: /api/rides/?sort=distance&lat=1.0&lon=14.000
        """
        sort = request.query_params.get('sort', 'pickup_time')
        lat = request.query_params.get('lat')
        lon = request.query_params.get('lon')

        qs = self.get_queryset()

        if sort == 'pickup_time':
            qs = qs.order_by('-pickup_time')
        elif sort == 'distance':
            if not lat or not lon:
                return Response(
                    {"detail": "lat and lon are required for distance sorting"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            lat, lon = float(lat), float(lon)

            qs = filter_nearby(qs, lat, lon)
            qs = annotate_distance(qs, lat, lon).order_by('distance')
        else:
            return Response({"Error": "Invalid parameters"}, status=status.HTTP_400_BAD_REQUEST)
        
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

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

from django.db.models import F, Prefetch, Window
from django.db.models.functions import RowNumber

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

# API app
from api.permissions import IsAdmin
from api.models import Ride, RideEvent
from api.serializers import RideSerializer

# Helper defs
from api.helpers import annotate_distance, filter_nearby

# utils
from django.utils import timezone
from datetime import timedelta

class RideViewset(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def get_queryset(self):
        """
        - This prevents fetching full RideEvent lists and avoids N+1 queries
        - I've limit the RideEvent list to 10 events
        """
        cutoff = timezone.now() - timedelta(hours=24)

        prefetch_qs = (
            RideEvent
            .objects
            .filter(created_at__gte=cutoff)
            .annotate(
                row_number=Window(
                    expression=RowNumber(),
                    partition_by=[F('id_ride')],
                    order_by=F('created_at').desc()
                )
            )
            .filter(row_number__lte=10)
            .order_by('-created_at')
        )

        return (
            Ride.objects
                .prefetch_related(
                    Prefetch(
                        'ride_events', 
                        queryset=prefetch_qs, 
                        to_attr='todays_ride_events'
                    )
                )
        )

    def list(self, request, *args, **kwargs):
        """
        Default sorting is pickup_time when there is no sort query param
        distance url sample: /api/rides/?sort=distance&lat=1.0&lon=14.000
        rider email url sample: /api/rides/?sort=rider-email&email=dutch@gmail.com
        status url sample: /api/rides/?sort=ride-status&status=dropoff
        """
        sort = request.query_params.get('sort', 'pickup_time')
        lat = request.query_params.get('lat')
        lon = request.query_params.get('lon')
        email = request.query_params.get('email')
        rideStatus = request.query_params.get('status')

        qs = self.get_queryset()

        if sort == 'pickup-time':
            qs = qs.order_by('-pickup_time')
        elif sort == 'rider-email':
            if not email:
                return Response(
                    {"detail": "email is required for email sorting"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            qs = qs.filter(id_rider__email=email)
        elif sort == 'ride-status':
            if not rideStatus:
                return Response(
                    {"detail": "status is required for ride status sorting"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            qs = qs.filter(status=rideStatus)
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
            return Response(
                {"Error": "Invalid query parameters"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

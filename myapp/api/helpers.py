from math import radians
from django.db.models import F, Value, FloatField
from django.db.models.functions import Sin, Cos, ACos, Radians

def annotate_distance(qs, lat, lon):
    """
    Haversine formula to calculate the distance between 2 points
    Earth radius:
    6371 * angle → distance in kilometers
    3959 * angle → distance in miles
    """
    lat_radians = radians(lat)
    lon_radians = radians(lon)
    return qs.annotate(
        distance=6371 * ACos(
            Sin(Value(lat_radians)) * Sin(Radians(F('pickup_latitude'))) +
            Cos(Value(lat_radians)) * Cos(Radians(F('pickup_latitude'))) *
            Cos(Radians(F('pickup_longitude')) - Value(lon_radians))
        )
    )

def filter_nearby(qs, lat, lon, max_deg=0.5):
    """
    Optional bounding box filter (~55 km per 0.5 degrees)
    to reduce scan cost in large SQLite tables.
    """
    return qs.filter(
        pickup_latitude__range=(lat - max_deg, lat + max_deg),
        pickup_longitude__range=(lon - max_deg, lon + max_deg),
    )

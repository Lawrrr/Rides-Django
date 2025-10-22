from django.db import models
from .ride import Ride

class Ride_Event(models.Model):
    id_ride_event = models.IntegerField(primary_key=True)
    id_ride = models.ForeignKey(Ride, null=False, on_delete=models.CASCADE)
    description = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

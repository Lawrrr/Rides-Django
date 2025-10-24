from django.db import models
from .ride import Ride

class RideEvent(models.Model):
    id_ride_event = models.AutoField(primary_key=True)
    id_ride = models.ForeignKey(Ride, null=False, on_delete=models.CASCADE, related_name="ride_events")
    description = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id_ride_event} - {self.description}"

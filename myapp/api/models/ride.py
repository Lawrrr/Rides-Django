from django.db import models
from .user import User

class Ride(models.Model):
    id_ride = models.AutoField(primary_key=True)
    status = models.CharField(max_length=100, null=False)
    id_rider = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name="user_rider")
    id_driver = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name="user_driver")
    pickup_latitude = models.FloatField(max_length=12)
    pickup_longitude = models.FloatField(max_length=12)
    dropoff_latitude = models.FloatField(max_length=12)
    dropoff_longitude = models.FloatField(max_length=12)

    def __str__(self):
        return f"{self.id_ride} - {self.status}"

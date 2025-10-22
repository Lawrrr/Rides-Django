from django.db import models

class User(models.Model):
    id_user = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=100, null=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

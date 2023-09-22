from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class LoftProfile(models.Model):
    loft_id = models.OneToOneField(User, max_length=7, on_delete=models.CASCADE, null=True)
    loft_name = models.CharField(max_length=30)
    mobile_number = models.CharField(max_length=13)
    latitude = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    longitude = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    description = models.CharField(blank=True, max_length=300)

    def __str__(self):
        return self.loft_name


class RegProfile(models.Model):
    loft_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=4)
    mobile_number = models.CharField(max_length=13)
    email = models.EmailField()

    def __str__(self):
        return self.loft_name

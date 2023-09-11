from django.db import models
from profiles.models import LoftProfile
from race.models import Race


class Roll(models.Model):
    code = models.CharField(primary_key=True, max_length=4, unique=True)
    key = models.CharField(max_length=4, unique=True, blank=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    loft = models.ForeignKey(LoftProfile, on_delete=models.CASCADE)
    distance = models.FloatField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=20, blank=True)
    registration_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code

from django.db import models


# Create your models here.
class Race(models.Model):
    race_id = models.CharField(primary_key=True, max_length=6, unique=True)
    name = models.CharField(max_length=50)
    date = models.DateField()
    coordinator = models.CharField(max_length=20)
    start_loc = models.CharField(max_length=30)
    start_time = models.DateTimeField(null=True, blank=True)
    latitude = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    longitude = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    cut_off = models.DateTimeField()
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


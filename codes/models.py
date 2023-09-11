from django.db import models


# Create your models here.
class Code(models.Model):
    code = models.CharField(primary_key=True, max_length=4, unique=True)
    key = models.CharField(max_length=4, unique=True, blank=True)

    def __str__(self):
        return self.code

from django.db import models

# Create your models here.
class Companies(models.Model):
    name = models.CharField(max_length=64)
    sector_id = models.PositiveIntegerField()
    sector = models.CharField(max_length=256)
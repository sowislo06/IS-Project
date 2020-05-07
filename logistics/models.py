from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from asset.models import Asset, Station


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    startDate = models.DateTimeField(default=timezone.now)
    endDate = models.DateTimeField(default=None, blank=True, null=True)
    fromStation = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='from_station')
    toStation = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='to_station')
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, default='')



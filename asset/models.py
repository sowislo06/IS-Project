from django.db import models



class Station(models.Model):
    name = models.CharField(max_length=250)
    max_cap = models.IntegerField()

class Category(models.Model):
    name = models.CharField(max_length=250)


class Asset(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )
    station = models.ForeignKey(
        'Station',
        on_delete=models.CASCADE,
    )

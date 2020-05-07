from django.db import models



class Station(models.Model):
    name = models.CharField(max_length=250)
    max_cap = models.IntegerField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


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
    def __str__(self):
        return self.name

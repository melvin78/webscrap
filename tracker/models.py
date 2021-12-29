from django.db import models


# Create your models here.
class UserTracker(models.Model):
    iduser_tracker = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    tracker_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user_tracker'


class Tracker(models.Model):
    idtracker = models.AutoField(primary_key=True)
    subcategory_id = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tracker'


class PriceChange(models.Model):
    name = models.TextField(blank=True, null=True)
    product = models.TextField(blank=True, null=True)
    initial_price = models.FloatField(blank=True, null=True)
    new_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'price_change'

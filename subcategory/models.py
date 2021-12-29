from django.db import models


# Create your models here.
class SubCategory(models.Model):
    idsub_category = models.AutoField(primary_key=True)
    category_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=155, blank=True, null=True)
    current_price = models.FloatField(blank=True, null=True)
    link = models.CharField(max_length=245, blank=True, null=True)
    image = models.CharField(max_length=245, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sub_category'

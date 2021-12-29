from django.db import models


# Create your models here.
class Videos(models.Model):
    idvideos = models.AutoField(primary_key=True)
    subcategory_id = models.IntegerField(blank=True, null=True)
    video = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'videos'

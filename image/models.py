from django.db import models


class Image(models.Model):
    idimage = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    subcateoryid = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'image'

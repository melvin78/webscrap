from django.db import models


class Categories(models.Model):
    idcategories = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=45)
    website_id = models.IntegerField(blank=True, null=True)
    link = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'categories'

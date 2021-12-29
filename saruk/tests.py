from django.test import TestCase

# Create your tests here.
from categories.models import Categories

item= Categories.objects.create(
category_name= "phone",
website_id="2",
link ="{'link':'saruk.co.ke'}"
)

item.save()


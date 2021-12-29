from django.contrib import admin

# Register your models here.
from image.models import Image

Image.objects.create(subcateoryid=1,
                     image='https://www.deccanherald.com/sites/dh/files/styles/article_detail/public/articleimages/2020/10/12/aiphone11-pro-camera-cs-1-768244-1602497450.png?itok=7UyQFMtH')

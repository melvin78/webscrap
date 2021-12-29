from django.contrib import admin

# Register your models here.
from videos.models import Videos
Videos.objects.create(
    subcategory_id=1,
    video='https://www.youtube.com/watch?v=OoY7zp8GkLI&t=42s'



)
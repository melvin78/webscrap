
from subcategory.models import SubCategory

r = SubCategory.objects.filter(idsub_category=2).get()
r.reviews['articles'].append('https://www.soundguys.com/apple-airpods-pro-review-27106/')
r.reviews['videos'].append('https://www.youtube.com/watch?v=cG8PXdTlDag')
r.save()




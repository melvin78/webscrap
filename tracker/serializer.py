from tracker import models
from rest_framework import serializers


class PriceChangeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PriceChange
        fields = ['name', 'product', 'initial_price', 'new_price']




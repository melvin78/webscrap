# from django.shortcuts import render
# from rest_framework import viewsets
# from tracker.models import PriceChange
# from tracker.serializer import PriceChangeSerializers
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import mixins,viewsets
#
#
# class PriceChangeViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
#
#     serializer_class = PriceChangeSerializers
#     queryset = PriceChange.objects.all()
#
#     def get_queryset(self):
#
#         queryset = PriceChange.objects.all()
#         idcat= self.kwargs['idcat']
#         if idcat is not None:
#             queryset = queryset.filter(new_price=idcat)
#         return queryset

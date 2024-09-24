from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Women, Category


class WomenAPIView(APIView):
    def get(self, request):
        lst = Women.objects.all()
        return Response({'posts': list(lst)})

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

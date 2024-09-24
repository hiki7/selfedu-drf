from django.shortcuts import render
from rest_framework import generics

from .models import Women, Category

class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

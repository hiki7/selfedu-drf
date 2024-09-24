from django.urls import path
from . import views

urlpatterns = [
    path('women/', views.WomenAPIView.as_view(), name='women'),
    path('women/<int:pk>/', views.WomenAPIView.as_view(), name='women-detail'),
]
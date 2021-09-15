"""
views.py
"""
from rest_framework import viewsets

from .serializers import HeroSerializer, PublisherSerializer, SuperPowerSerializer
from .models import Hero, Publisher, SuperPower


class HeroViewSet(viewsets.ModelViewSet): #ModelViewSet handles GET and POST
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class PublisherViewSet(viewsets.ModelViewSet): #ModelViewSet handles GET and POST
    queryset = Publisher.objects.all().order_by('creator')
    serializer_class = PublisherSerializer

class SuperPowerViewSet(viewsets.ModelViewSet): #ModelViewSet handles GET and POST
    queryset = SuperPower.objects.all().order_by('name')
    serializer_class = SuperPowerSerializer

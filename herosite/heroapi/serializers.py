"""
Serialize models to JSON
"""
from rest_framework import serializers

from .models import Hero, Publisher, SuperPower

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id','name', 'alias', 'publisher')

class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'creator')

class SuperPowerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SuperPower
        fields = ('id', 'name')

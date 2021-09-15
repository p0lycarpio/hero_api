# models.py

from django.db import models

class Publisher(models.Model):
    creator = models.CharField(max_length=80)
    def __str__(self):
        return self.creator

class Hero(models.Model):
    name = models.CharField(max_length=80)
    alias = models.CharField(max_length=80)
    publisher = models.ForeignKey(Publisher, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.name



class SuperPower(models.Model):
    name = models.CharField(max_length=80)
    heroes = models.ManyToManyField(Hero)
    def __str__(self):
        return self.name

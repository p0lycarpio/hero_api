from django.core.management.base import BaseCommand
from heroapi.models import Hero
import csv


class Command(BaseCommand):
    def handle(self, **options):
        with open('superheroes_nlp_dataset.csv', 'r') as read_obj:           
            herolist = [{k: v for k, v in row.items()}
                for row in csv.DictReader(read_obj, skipinitialspace=True)]

            for item in herolist:
                hero_params = {
                    "name": item['name'],
                    "alias": item['real_name'],
                    #"publisher": item['creator']
                }
                hero = Hero(**hero_params)
                hero.save()
                print(f"{hero.name} created !")


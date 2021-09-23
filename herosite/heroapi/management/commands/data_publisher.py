from django.core.management.base import BaseCommand
from heroapi.models import Publisher
import csv


class Command(BaseCommand):
    def handle(self, **options):
        Publisher.objects.all().delete()
        with open('superheroes_nlp_dataset.csv', 'r') as read_obj:           
            list = [{k: v for k, v in row.items()}
                for row in csv.DictReader(read_obj, skipinitialspace=True)]
            publisherlist = set()
            for item in list:
                publisherlist.add(item["creator"])
                #publisher.save()
                #print(f"{publisher.creator} created !")
            print(publisherlist)
            for publisher in publisherlist:
                p = Publisher(creator = publisher)
                p.save()
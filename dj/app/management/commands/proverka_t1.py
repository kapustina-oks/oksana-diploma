from app.models import First_tab
from django.core.management.base import BaseCommand
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('/Users/oksana/Downloads/1_t.csv', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=';')
            First_tab.objects.all().delete()
            for row in reader:
                try:
                    index_PBT= row[2]
                except Exception as e:
                    index_PBT = None
                try:
                    index_P = row[3]
                except Exception as e:
                    index_P = None
                try:
                    index_B = row[4]
                except Exception as e:
                    index_B = None
                try:
                    index_T = row[5]
                except Exception as e:
                    index_T = None

                First_tab(drug=row[0].lower(), ecol_risk=row[1], index_PBT=index_PBT,
                          index_P=index_P, index_B=index_B, index_T=index_T,
                          inactive_metabolite=row[6], inactivation_reagent=row[8]).save()
                print(row)


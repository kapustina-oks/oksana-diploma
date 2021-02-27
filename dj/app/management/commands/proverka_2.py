from app.models import Second_tab
from django.core.management.base import BaseCommand
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('/Users/oksana/Desktop/Книга2.csv', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=';')
            Second_tab.objects.all().delete()
            for row in reader:
                try:
                    lc50_c = float(row[1].replace(',', '.'))
                except Exception as e:
                    lc50_c = None
                try:
                    lc50_d = float(row[2].replace(',', '.'))
                except Exception as e:
                    lc50_d = None
                try:
                    coef_bioaccum = float(row[3].replace(',', '.'))
                except Exception as e:
                    coef_bioaccum = None
                try:
                    ld50 = float(row[4].replace(',', '.'))
                except Exception as e:
                    ld50 = None

                Second_tab(drug=row[0].lower(), lc50_c=lc50_c, lc50_d=lc50_d, coef_bioaccum=coef_bioaccum,  ld50=ld50).save()
                print(row)

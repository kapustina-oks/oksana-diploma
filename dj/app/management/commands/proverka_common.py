from app.models import Common_tad
from django.core.management.base import BaseCommand
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('/Users/oksana/Downloads/Пособие_по_химической_утилизации_основных_групп_фармацевтических.csv',
                  encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=';')
            Common_tad.objects.all().delete()
            for row in reader:
                try:
                    index_PBT = row[4]
                except Exception as e:
                    index_PBT = None
                try:
                    index_P = row[5]
                except Exception as e:
                    index_P = None
                try:
                    index_B = row[6]
                except Exception as e:
                    index_B = None
                try:
                    index_T = row[7]
                except Exception as e:
                    index_T = None
                try:
                    lc50_c_original = float(row[10].replace(',', '.'))
                except Exception as e:
                    lc50_c_original = None
                try:
                    lc50_c_product = row[11].replace(',', '.')
                    if not lc50_c_product:
                        lc50_c_product = None
                except Exception as e:
                    lc50_c_product = None
                try:
                    lc50_d_original = float(row[12].replace(',', '.'))
                except Exception as e:
                    lc50_d_original = None
                try:
                    lc50_d_product = row[13].replace(',', '.')
                    if not lc50_d_product:
                        lc50_d_product = None
                except Exception as e:
                    lc50_d_product = None
                try:
                    coef_bioaccum_original = float(row[14].replace(',', '.'))
                except Exception as e:
                    coef_bioaccum_original = None
                try:
                    coef_bioaccum_product = row[15].replace(',', '.')
                    if not coef_bioaccum_product:
                        coef_bioaccum_product = None
                except Exception as e:
                    coef_bioaccum_product = None
                    # print(e)
                    # print('Failed on: ')
                    # print(row[15])
                try:
                    ld50_original = float(row[16].replace(',', '.'))
                except Exception as e:
                    ld50_original = None
                try:
                    ld50_product = row[17].replace(',', '.')
                    if not ld50_product:
                        ld50_product = None
                except Exception as e:
                    ld50_product = None

                if not row[0]:
                    break

                
                Common_tad(drug=row[1].lower(),group_ath=row[0], commercial_name=row[2], ecol_risk=row[3], index_PBT=index_PBT,
                           index_P=index_P, index_B=index_B, index_T=index_T,
                           inactive_metabolite=row[8], inactivation_reagent=row[9], lc50_c_original=lc50_c_original,
                           lc50_c_product=lc50_c_product, lc50_d_original=lc50_d_original, lc50_d_product=lc50_d_product,
                           coef_bioaccum_original=coef_bioaccum_original, coef_bioaccum_product=coef_bioaccum_product,
                           ld50_original=ld50_original, ld50_product=ld50_product).save()
                print(row)



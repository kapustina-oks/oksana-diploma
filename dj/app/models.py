from django.db import models

# class Drags(models.Model):
#     name_of_drags = models.CharField(max_length=300)
#     class_of_danger = models.CharField(max_length=1)
#     way_of_recycling = models.CharField(max_length=600)

class First_tab(models.Model):
    drug = models.CharField(max_length=50)
    ecol_risk = models.CharField(max_length=50)
    index_PBT = models.CharField(max_length=5, null=True)
    index_P = models.CharField(max_length=5, null=True)
    index_B = models.CharField(max_length=5, null=True)
    index_T = models.CharField(max_length=5, null=True)
    inactive_metabolite = models.CharField(max_length=500)
    inactivation_reagent = models.CharField(max_length=500)

class Second_tab(models.Model):
    drug = models.CharField(max_length=50)
    lc50_c = models.FloatField(null=True)
    lc50_d = models.FloatField(null=True)
    coef_bioaccum = models.FloatField(null=True)
    ld50 = models.FloatField(null=True)

class Common_tad(models.Model):
    group_ath = models.CharField(max_length=1000)
    drug = models.CharField(max_length=50)
    commercial_name = models.CharField(max_length=1000)
    ecol_risk = models.CharField(max_length=50)
    index_PBT = models.CharField(max_length=5, null=True)
    index_P = models.CharField(max_length=5, null=True)
    index_B = models.CharField(max_length=5, null=True)
    index_T = models.CharField(max_length=5, null=True)
    inactive_metabolite = models.CharField(max_length=500)
    inactivation_reagent = models.CharField(max_length=500)
    lc50_c_original = models.FloatField(null=True)
    lc50_c_product = models.CharField(max_length=1000, null=True)
    lc50_d_original = models.FloatField(null=True)
    lc50_d_product = models.CharField(max_length=1000, null=True)
    coef_bioaccum_original = models.FloatField(null=True)
    coef_bioaccum_product = models.CharField(max_length=1000, null=True)
    ld50_original = models.FloatField(null=True)
    ld50_product = models.CharField(max_length=1000, null=True)
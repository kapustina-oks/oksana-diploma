from django.db import models

class First_tab(models.Model):
    drug = models.CharField(max_length=50)
    ecol_risk = models.CharField(max_length=50)
    index_PBT = models.IntegerField(default=0)
    index_P = models.IntegerField(default=0)
    index_B = models.IntegerField(default=0)
    index_T = models.IntegerField(default=0)
    inactive_metabolite = models.CharField(max_length=500)
    inactivation_reagent = models.CharField(max_length=500)

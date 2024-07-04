from django.db import models


class Load(models.Model):

    ds = models.DateTimeField()
    business_line = models.CharField(max_length=200)
    sector = models.CharField(max_length=200)
    skill_group = models.CharField(max_length=200)
    channel = models.CharField(max_length=200)
    transactions = models.FloatField()
    aht = models.FloatField()
    asa = models.FloatField()
    interval = models.FloatField()
    shrinkage = models.FloatField()
    version = models.DateField()

    class Meta:
        managed = False
        db_table = 'usr_fcst\".\"skuld_test'
        
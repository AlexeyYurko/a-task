from django.db import models


# Create your models here.

# date,channel,country,os,impressions,clicks,installs,spend,revenue


class Record(models.Model):
    date = models.DateField(null=True, blank=True)
    channel = models.CharField(
        verbose_name='channel', max_length=30, blank=True, default='')
    country = models.CharField(
        verbose_name='country', max_length=2, blank=True, default='')
    os = models.CharField(
        verbose_name='os', max_length=7, blank=True, default='')
    impressions = models.IntegerField(
        verbose_name='impressions', default=0)
    clicks = models.IntegerField(
        verbose_name='clicks', default=0)
    installs = models.IntegerField(
        verbose_name='installs', default=0)
    spend = models.FloatField(verbose_name='spend', default=0)
    revenue = models.FloatField(verbose_name='revenue', default=0)
    cpi = models.FloatField(verbose_name='cpi', default=0)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UMTF(models.Model):
    value = models.CharField(max_length=4)

    def __str__(self):
        return self.value


class Trade(models.Model):
    umtf = models.ForeignKey(UMTF)
    timestamp = models.DateTimeField(db_index=True)
    amount = models.FloatField(default=0.0)
    currency = models.CharField(max_length=3)

    @property
    def umtf_code(self):
        return self.umtf.value


class LatestTrade(models.Model):
    """
    Denormalised for query speed.
    
    Using Django Model for compatibility with django_cachedpaginator
    Given the appropriate time resources, would use a custom paginator and a cache
    to reduce database load for such warm data
    """
    umtf = models.CharField(max_length=4, unique=True)
    amount = models.FloatField(default=0.0)
    currency = models.CharField(max_length=3)

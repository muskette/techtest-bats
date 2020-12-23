# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView
from django_cachedpaginator.views import CachedPaginatorViewMixin

from umtf.models import LatestTrade


class ListMostRecentTradesView(CachedPaginatorViewMixin, ListView):
    paginate_by = 15
    queryset = LatestTrade.objects.all().order_by('umtf')
    template_name = 'latest_umtf_trades.html'

    def get_cache_key(self):
        """Required for django_cachedpaginator"""
        return 'latest_trades'

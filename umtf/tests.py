# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from umtf.models import UMTF, LatestTrade
from umtf.tasks import update_latest_stock_values


class TestLatestStockUpdate(TestCase):

    def setUp(self):
        super(TestLatestStockUpdate, self).setUp()

    def tearDown(self):
        super(TestLatestStockUpdate, self).tearDown()
        LatestTrade.objects.all().delete()

    def test_update_gets_all_umtfs(self):
        total_umtfs = UMTF.objects.count()
        update_latest_stock_values()
        total_stock_prices = LatestTrade.objects.count()
        self.assertEquals(total_stock_prices, total_umtfs)

    def test_no_new_db_entries_on_Exception(self):
        raise NotImplementedError()


class TestLoadFixtures(TestCase):

    def test_loads_all_umtfs_from_file(self):
        filename = 'fixtures/cac_idx.csv'
        line_count = 0
        with open(filename, 'r') as f:
            line_count = sum(1 for l in f)
        row_count = UMTF.objects.count()
        self.assertEquals(line_count, row_count)

    def test_parse_hour_minute_from_filename(self):
        raise NotImplementedError()

    def test_loads_all_trades_from_file(self):
        raise NotImplementedError()

    def test_no_new_db_entries_on_Exception(self):
        raise NotImplementedError()


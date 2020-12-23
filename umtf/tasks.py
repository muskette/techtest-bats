from datetime import timedelta

from celery.task import periodic_task
from django.db import transaction

from umtf.models import Trade, LatestTrade, UMTF


@periodic_task(run_every=timedelta(minutes=1))
def update_latest_stock_values():
    with transaction.atomic():
        # Using a dict comprehension to store umtfs
        # because x.umtf_code on line 20 would result in a new db read for each umtf row
        # if a RawQueryset wasn't being used, prefetch_related would be the function to use to prevent this
        umtfs = {u.value: u.pk for u in UMTF.objects.all()}

        # Using a RawQuerySet as this query cannot be done with QuerySets when the db backend is SQLite
        latest_trades = Trade.objects.raw(
            'SELECT * FROM umtf_trade GROUP BY umtf_id HAVING timestamp=Max(timestamp)'
        )

        LatestTrade.objects.all().delete()
        lt = [
            LatestTrade(umtf=umtfs[x.umtf_id], amount=x.amount, currency=x.currency)
            for x in latest_trades
        ]
        LatestTrade.objects.bulk_create(lt)

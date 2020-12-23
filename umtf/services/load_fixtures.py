import csv
from datetime import datetime, time, date, timedelta

from umtf.models import UMTF, Trade

def load_umtfs(filename):
    with open(filename) as csvfile:
        file = csv.reader(csvfile)
        umtfs = [UMTF(value=x[0]) for x in file]
    UMTF.objects.bulk_create(umtfs)


def parse_filename(filename):
    format24h = filename.split('_')[2].split('.')[0]
    hour = format24h[:2]
    minute = format24h[2:]
    return hour, minute


def load_trade_file(filename):
    hour, minute = parse_filename(filename)
    t = time(hour=int(hour), minute=int(minute))
    d = date.today()
    timestamp = datetime.combine(d,t)
    umtfs = {u.value: u.pk for u in UMTF.objects.all()}
    with open(filename) as csvfile:
        file = csv.reader(csvfile)
        trades = []
        for row in file:
            trades.append(
                Trade(
                    umtf_id=umtfs[row[0]],
                    timestamp=timestamp,
                    amount=float(row[1]),
                    currency=row[2]
                )
            )
    Trade.objects.bulk_create(trades)

def load_trades(filenames):
    for filename in filenames:
        load_trade_file(filename)

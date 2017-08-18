# -*- coding: utf-8-*-

import random
from datetime import datetime, timedelta


def perdelta(start, end):
    curr = start
    delta = timedelta()
    while curr < end:
        curr += delta
        yield curr
        delta = timedelta(hours=random.randint(1, 30))


for dt in perdelta(datetime(2017, 05, 01, 11, 12, 11), datetime.today(), 2):
   print dt

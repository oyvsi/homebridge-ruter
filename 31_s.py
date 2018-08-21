#!/usr/bin/python3
import ruter
from datetime import datetime, timezone

def rreplace(s, old, new, count):
    return (s[::-1].replace(old[::-1], new[::-1], count))[::-1]

sofienberg = 3010533
r = ruter.Ruter()
nextbus = r.get_next_departure(sofienberg, '31', 2)
departure = nextbus['MonitoredCall']['ExpectedDepartureTime']
departure = rreplace(departure, ':', '', 1)
ts = datetime.strptime(departure, '%Y-%m-%dT%H:%M:%S%z')
now = datetime.now(timezone.utc)
delta = (ts - now).seconds

print(delta)

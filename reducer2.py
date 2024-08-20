#!/usr/bin/python
import sys
import heapq
import os

from_hour = int(os.environ['FROM_HOUR'])
to_hour = int(os.environ['TO_HOUR'])

current_hour = None
ip_count_heap = []

for line in sys.stdin:
    line = line.strip()
    hour_ip, count = line.split('\t', 1)
    hour, ip = hour_ip[1:].split(']', 1)
    hour = int(hour)
    count = int(count)

    if from_hour <= hour < to_hour:
        if hour != current_hour:
            if current_hour is not None:
                top_ip_counts = heapq.nlargest(3, ip_count_heap)
                for ic in top_ip_counts:
                    print('%s\t%s:%s' % (current_hour, ic[1], ic[0]))
            current_hour = hour
            ip_count_heap = []
        heapq.heappush(ip_count_heap, (count, ip))

if from_hour <= hour < to_hour:
    top_ip_counts = heapq.nlargest(3, ip_count_heap)
    for ic in top_ip_counts:
        print('%s\t%s:%s' % (current_hour, ic[1], ic[0]))
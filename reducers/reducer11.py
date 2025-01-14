#!/usr/bin/python
import sys
import heapq

current_hour = None
ip_count_heap = []

for line in sys.stdin:
    line = line.strip()
    hour_ip, count = line.rsplit("\t", 1)
    hour, ip = hour_ip[1:].split("]", 1)
    count = int(count)

    if hour != current_hour:
        if current_hour is not None:
            top_ip_counts = heapq.nlargest(3, ip_count_heap)
            for ic in top_ip_counts:
                print('%s\t%s:%s' % (current_hour, ic[1], ic[0]))
        current_hour = hour
        ip_count_heap = []

    heapq.heappush(ip_count_heap, (count, ip))

if current_hour == hour:
    top_ip_counts = heapq.nlargest(3, ip_count_heap)
    for ic in top_ip_counts:
        print('%s\t%s:%s' % (current_hour, ic[1], ic[0]))

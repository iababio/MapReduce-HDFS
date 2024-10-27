#!/usr/bin/python
import sys

current_key = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    key, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    if current_key == key:
        current_count += count
    else:
        if current_key:
            print('%s\t%s' % (current_key, current_count))
        current_key = key
        current_count = count

if current_key is not None:  # Change here to check if current_key is defined
    print('%s\t%s' % (current_key, current_count))

#!/usr/bin/python
import sys
import re
import os

from_hour = int(os.environ['FROM_HOUR'])
to_hour = int(os.environ['TO_HOUR'])

pattern = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\[(\d+)/[a-zA-Z]+/\d{4}:(?P<hour>\d{2}):\d{2}:\d{2}.*')

for line in sys.stdin:
    match = pattern.search(line)
    if match:
        hour = int(match.group('hour'))
        if from_hour <= hour < to_hour:
            print('%s\t%s' % ('[' + match.group('hour') + ']' + match.group('ip'), 1))

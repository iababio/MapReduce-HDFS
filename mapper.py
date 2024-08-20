#!/usr/bin/python
import sys
import re

pattern = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\[(\d+)/[a-zA-Z]+/\d{4}:(?P<hour>\d{2}):\d{2}:\d{2}.*')

for line in sys.stdin:
    match = pattern.search(line)
    if match:
        print '%s\t%s' % ('[' + match.group('hour') + ']' + match.group('ip'), 1)
#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    print('%s\t%s' % (line, 1))

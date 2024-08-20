#!/usr/bin/python
import os
import sys

# Get user input
args = sys.argv
if len(args) != 2 or len(args[1].split("-")) != 2:
    print("Incorrect usage. Please provide the range in the format 'start_hour-end_hour', where start_hour < end_hour. Example: '0-1'")
    sys.exit(1)

from_hour, to_hour = map(int, args[1].split("-"))

if from_hour >= to_hour:
    print("Invalid range. Ensure start_hour < end_hour.")
    sys.exit(1)

os.environ["FROM_HOUR"] = str(from_hour)
os.environ["TO_HOUR"] = str(to_hour)

# Run MapReduce
os.system("cat ../../mapreduce-test-data/access.log | python mapper1.py | sort -k1,1 | python reducer1.py > intermediate_results.txt")
os.system("cat intermediate_results.txt | python reducer2.py")
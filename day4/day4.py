# https://adventofcode.com/2018/day/4

from datetime import datetime
import re
import sys

def parse_record(record):
    # ex: [1518-11-01 00:00] Guard #10 begins shift
    date_str = re.search('\[(.*?)\]', record).group(1)
    log_time = datetime.strptime(date_str, '%Y-%m-%d %H:%M')
    return log_time
    

def log_sleep_times(parsed_record):
    pass

def process_records(filename):
    records = open(filename).read().splitlines()
    records.sort()
    return records

# process_records(sys.argv[1])

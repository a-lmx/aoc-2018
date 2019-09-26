# https://adventofcode.com/2018/day/4

from datetime import datetime
import re
import sys

def parse_record(record):
    # ex: [1518-11-01 00:00] Guard #10 begins shift
    record_dict = {}
    date_str = re.search('\[(.*?)\]', record).group(1)
    record_dict['log_time'] = datetime.strptime(date_str, '%Y-%m-%d %H:%M')
    record_dict['note'] = record.split('] ')[1].split()
    return record_dict

def log_sleep_time(time_log, guard_id, asleep_time, wake_time):
    if guard_id in time_log:
        guard_log = time_log[guard_id]
    else:
        guard_log = [0 for i in range(60)]
        time_log[guard_id] = guard_log
    for i in range(wake_time - asleep_time):
        guard_log[asleep_time + i] += 1

def find_sleepiest_guard(time_log):
    sleepiest_guard = None
    most_sleeping_mins = 0
    for guard in time_log:
        sleeping_mins = sum(time_log[guard])
        if sleeping_mins > most_sleeping_mins:
            most_sleeping_mins = sleeping_mins
            sleepiest_guard = guard
    return sleepiest_guard

def find_sleepiest_minute(minute_list):
    most_sleeping_mins = 0
    sleepiest_minute = None
    for i in range(len(minute_list)):
        if minute_list[i] > most_sleeping_mins:
            most_sleeping_mins = minute_list[i]
            sleepiest_minute = i
    return sleepiest_minute

def process_records(filename):
    records = open(filename).read().splitlines()
    records.sort()
    time_log = {}
    guard_id = None
    asleep_time = None

    for record in records:
        parsed_record = parse_record(record)
        log_time = parsed_record['log_time']
        note = parsed_record['note']
        if len(note) == 4: # note is guard change
            guard_id = note[1][1:]
            asleep_time = None
        if note[1] == 'asleep':
            asleep_time = log_time.minute
        if note[0] == 'wakes':
            wake_time = log_time.minute
            log_sleep_time(time_log, guard_id, asleep_time, wake_time)

    sleepiest_guard = find_sleepiest_guard(time_log)
    sleepiest_minute = find_sleepiest_minute(time_log[sleepiest_guard])
    print(f'The sleepiest guard is {sleepiest_guard}. They were most often asleep at minute {sleepiest_minute}.')
    print(f'The product of the sleepiest guard\'s id and their sleepiest minute is {int(sleepiest_guard) * sleepiest_minute}.')

process_records(sys.argv[1])

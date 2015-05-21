import re
from dateutil.parser import parse
# from datetime import datetime

DATE_REGEX = re.compile('\w+-\w+-\w+:\w+:\w+-\w+')


def parse_file(filename):
    with open(filename, 'r') as f:
        raw_text = f.read()
    dates = DATE_REGEX.findall(raw_text)
    recordings = DATE_REGEX.split(raw_text)[1:]
    assert len(dates) == len(recordings)
    parsed_data = [parse_recording(recording) for recording in recordings]
    ping = []
    download = []
    upload = []
    for data in parsed_data:
        ping.append(data[0])
        download.append(data[1])
        upload.append(data[2])
    return {"date": [parse_date(date) for date in dates],
            "ping": ping,
            "download": download,
            "upload": upload}


def parse_recording(recording):
    if not recording.strip() or 'speedtest' in recording:
        return [None]*3
    record = recording.split('\n')[1:-1]
    numbers = [float(stat.split(' ')[1]) for stat in record]
    return numbers


def parse_date(date_string):
    # return datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S%z')
    return parse(date_string)

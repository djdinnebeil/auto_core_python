from datetime import datetime
from clipboard import print_to_screen

def get_timestamp():
    now = datetime.now()
    hour, minute = now.hour, now.minute
    if hour == 0:
        return f'00:{minute:02d}'
    elif 1 <= hour < 10:
        return f'0{hour}:{minute:02d}'
    elif 10 <= hour < 22:
        return f'{hour if hour <= 12 else hour - 12}:{minute:02d}'
    else:
        return f'{hour:02d}:{minute:02d}'

def get_short_datestamp_windows():
    now = datetime.now()
    return f'{now.month}-{now.day}-{now.strftime("%y")}'

def print_timestamp():
    print_to_screen(get_timestamp())
import sqlite3
from clock import get_short_datestamp_windows, get_timestamp
from clipboard import print_to_screen

episode_title = 'Link'
padding = 3
db_path=r'C:\DJ\Auto Core Python\db\link.db'

def pad_number(num):
    """
    Pad a number with leading zeroes up to the specified length.
    If the number's length is greater than or equal to the specified length, return as string without padding.
    """
    num_str = str(num)
    if len(num_str) >= padding:
        return num_str
    return num_str.zfill(padding)

def retrieve_and_increment_episode_number():
    print(db_path)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Read the current number
    cur.execute('SELECT number FROM episode LIMIT 1')
    result = cur.fetchone()
    if result is None:
        conn.close()
        raise ValueError('No value found in the database.')
    current_value = result[0]

    # Increment the number
    new_value = current_value + 1

    # Update the number in the database
    cur.execute('UPDATE episode SET number = ? WHERE number = ?', (new_value, current_value))
    conn.commit()
    conn.close()

    return current_value

def print_episode_title():
    episode_number = pad_number(retrieve_and_increment_episode_number())
    title = f'{episode_title} {episode_number}\n{get_short_datestamp_windows()}\n\n{get_timestamp()}'
    print_to_screen(title)

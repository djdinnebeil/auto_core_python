from pynput import keyboard
import time
import pyautogui
import pyperclip
from clipboard import copy_to_clipboard, paste_from_clipboard
import random
from datetime import datetime
import pygetwindow as gw
from journal import *
from clock import print_timestamp

function_key_activated = False
last_key_pressed = None

vk_numpad_map = {
    96: 'numpad_0',
    97: 'numpad_1',
    98: 'numpad_2',
    99: 'numpad_3',
    100: 'numpad_4',
    101: 'numpad_5',
    102: 'numpad_6',
    103: 'numpad_7',
    104: 'numpad_8',
    105: 'numpad_9'
}

try:
    auto_core_window = gw.getWindowsWithTitle('Auto Core Python')[0]
except IndexError:
    auto_core_window = None

def close_program():
    if auto_core_window:
        auto_core_window.close()

def on_press(key):
    global function_key_activated, last_key_pressed

    try:
        vk = key.vk
    except AttributeError:
        return

    if vk == 96:  # numpad_0 toggles function mode
        function_key_activated = not function_key_activated
        print('function key', 'activated' if function_key_activated else 'deactivated')
    elif vk == 97:  # numpad_1
        close_program() if function_key_activated else activate_Auto_Core()
    elif vk == 98:
        print('select_choice(Jose)') if function_key_activated else activate_Word()
    elif vk == 99:
        print('activate_Firefox()') if function_key_activated else close_program()
    elif vk == 100:
        print('Spotify_prev_song()') if function_key_activated else print_Daniel_choice()
    elif vk == 101:
        print('play_pause_Spotify()') if function_key_activated else print('play_pause_iTunes()')
    elif vk == 102:
        print('activate_iTunes()') if function_key_activated else print('next_song()')
    elif vk == 103:
        print('activate_Chrome()') if function_key_activated else print_to_screen('Hi GPT-4, this is DJ. I am studying software engineering.')
    elif vk == 104:
        print('print_military_timestamp_with_the_am_pm_timestamp()') if function_key_activated else print('select_choice(Lily)')
    elif vk == 105:
        print_Lily_choice() if function_key_activated else print_timestamp()

    # Auto-deactivate the function key after use
    if function_key_activated and (vk != 200 and vk != 96):
        function_key_activated = False

    last_key_pressed = vk


print('Program ready')
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

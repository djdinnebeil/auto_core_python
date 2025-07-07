from pynput import keyboard
import time
import pyautogui
import pyperclip
from clipboard import copy_to_clipboard, paste_from_clipboard, copy_and_paste_no_linebreak
import random
from datetime import datetime
import pygetwindow as gw
from journal import *
from clock import print_timestamp
from link import print_episode_title
from env import openai_api_key, copy_openai_api_key

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
        activate_Auto_Core() if not function_key_activated else close_program()
    elif vk == 98:
        activate_Word() if not function_key_activated else print('select_choice(Jose)')
    elif vk == 99:
        copy_openai_api_key() if not function_key_activated else print('activate_Firefox()')
    elif vk == 100:
        print_Daniel_choice(2) if not function_key_activated else print('Spotify_prev_song()')
    elif vk == 101:
        print_Daniel_choice(3)  if not function_key_activated else print('play_pause_Spotify()')
    elif vk == 102:
        print_Daniel_choice(4) if not function_key_activated else print('activate_iTunes()')
    elif vk == 103:
        copy_and_paste_no_linebreak('Hi GPT-4, this is DJ. I am studying software engineering.') if not function_key_activated else print(
            'activate_Chrome()')
    elif vk == 104:
        print_episode_title() if not function_key_activated else print_Star_choice()
    elif vk == 105:  # numpad_9
        print_timestamp() if not function_key_activated else print_Lily_choice()

    # Auto-deactivate the function key after use
    if function_key_activated and (vk != 200 and vk != 96):
        function_key_activated = False

    last_key_pressed = vk


print('Program ready')
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

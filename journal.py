import pygetwindow as gw
from taskbar import *
import random
from clipboard import *
import pyautogui
import time


def save_current_word_document():
    pyautogui.keyDown('ctrlleft')
    pyautogui.press('s')
    pyautogui.keyUp('ctrlleft')

def switch_back_to_last_open_window():
    pyautogui.keyDown('altright')
    pyautogui.press('tab')
    pyautogui.keyUp('altright')

def print_choice_with_name(name, number_of_choices=2):
    # original_window = gw.getActiveWindow()
    # activate_Auto_Core()
    number_of_choices = 2
    try:
        # number_of_choices = int(input('Please enter the number of choices: '))
        number_selection = random.randint(1, number_of_choices)
    except ValueError:
        number_of_choices = 2
        number_selection = random.randint(1, number_of_choices)
    selection = f'{name} selects {number_selection}.'
    # original_window.activate()
    print_to_screen(selection)

def print_Lily_choice():
    print_choice_with_name('Lily')

def print_Daniel_choice(number_of_choices=2):
    start = time.time()
    print_choice_with_name('Daniel', number_of_choices)
    print(f'Elapsed: {time.time() - start:.2f} seconds')

def print_Star_choice():
    print_choice_with_name('Star')

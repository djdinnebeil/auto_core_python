import pygetwindow as gw
from taskbar import *
import random
from clipboard import *
import pyautogui

def save_current_word_document():
    pyautogui.keyDown('ctrlleft')
    pyautogui.press('s')
    pyautogui.keyUp('ctrlleft')

def print_choice_with_name(name):
    original_window = gw.getActiveWindow()
    activate_Auto_Core()
    try:
        number_of_choices = int(input('Please enter the number of choices: '))
    except ValueError:
        number_of_choices = 2
    selection = f'{name} selects {random.randint(1, number_of_choices)}.'
    original_window.activate()
    print_to_screen(selection)

def print_Daniel_choice():
    print_choice_with_name('Daniel')

def print_Lily_choice():
    print_choice_with_name('Lily')
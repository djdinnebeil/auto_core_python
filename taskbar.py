import pyautogui
import pygetwindow as gw



def press_winkey_and_number(number):
    pyautogui.keyDown('winright')
    pyautogui.press(f'{number}')
    pyautogui.keyUp('winright')

def activate_Auto_Core():
    press_winkey_and_number(1)

def activate_Word():
    press_winkey_and_number(3)

import pyperclip
import pyautogui

pyautogui.FAILSAFE = False  # The failsafe only concerns mouse activity, so set to False

def copy_to_clipboard(text: str):
    """Copy the given text to the system clipboard."""
    pyperclip.copy(text)

def paste_from_clipboard():
    pyautogui.keyDown('ctrlleft')
    pyautogui.press('v')
    pyautogui.keyUp('ctrlleft')

def copy_and_paste_no_linebreak(text):
    pyperclip.copy(text)
    paste_from_clipboard()

def print_to_screen(message):
    print(message)
    pyperclip.copy(message + '\n\n')
    paste_from_clipboard()

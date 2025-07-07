import os
from dotenv import load_dotenv
from clipboard import copy_to_clipboard, paste_from_clipboard

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

def copy_openai_api_key():
    copy_to_clipboard(openai_api_key)
    paste_from_clipboard()
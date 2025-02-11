import json
import os
import sys
import msvcrt
import time
from contextlib import contextmanager

def get_app_dir():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    else:
        return os.path.expanduser('~')

APP_DIR = os.path.join(get_app_dir(), 'SMART_QUESTIONS')
CONFIG_FILENAME = 'config.json'
CONFIG_FILE = os.path.join(APP_DIR, CONFIG_FILENAME)

@contextmanager
def file_lock(file_obj):
    while True:
        try:
            msvcrt.locking(file_obj.fileno(), msvcrt.LK_LOCK, 1)
            yield
            break
        except IOError as e:
            if e.errno != 13:  # errno 13 is permission denied
                raise
            time.sleep(0.1)
    try:
        msvcrt.locking(file_obj.fileno(), msvcrt.LK_UNLCK, 1)
    except IOError:
        pass  # If unlocking fails, we can't do much about it

def set_config_value(key, value):
    os.makedirs(APP_DIR, exist_ok=True)
    
    try:
        with open(CONFIG_FILE, 'r+') as f:
            with file_lock(f):
                f.seek(0)
                try:
                    config = json.load(f) if os.path.getsize(CONFIG_FILE) > 0 else {}
                except json.JSONDecodeError:
                    config = {}
                
                config[key] = value
                
                f.seek(0)
                f.truncate()
                json.dump(config, f, indent=4)
    except PermissionError:
        print(f"Error: Unable to write to {CONFIG_FILE}. Check file permissions.")
    except IOError as e:
        print(f"Error accessing the config file: {e}")

def get_config_value(key, default=None):
    if not os.path.exists(CONFIG_FILE):
        return default
    
    try:
        with open(CONFIG_FILE, 'r') as f:
            with file_lock(f):
                if os.path.getsize(CONFIG_FILE) > 0:
                    try:
                        config = json.load(f)
                        return config.get(key, default)
                    except json.JSONDecodeError:
                        return default
                else:
                    return default
    except PermissionError:
        print(f"Error: Unable to read from {CONFIG_FILE}. Check file permissions.")
        return default
    except IOError as e:
        print(f"Error accessing the config file: {e}")
        return default


def auto_open_folder():
    HOME_DIR = os.path.expanduser('~')
    DOCUMENTS_DIR = os.path.join(HOME_DIR, 'Documents')
    APP_DIR = os.path.join(DOCUMENTS_DIR, 'SMART_QUESTIONS')
    
    try:
        os.startfile(APP_DIR)
    except Exception as e:
        print(f"Error opening folder: {e}")
        


def resource_path(relative_path):
    """
    Get the correct path for resources, works both for development
    and for PyInstaller bundled applications.
    
    Args:
    relative_path (str): The relative path to the resource file.
    
    Returns:
    str: The absolute path to the resource file.
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # If not running as bundled exe, use the script's directory
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


set_config_value("system_prompt_type", "I am a student and I need help with my homework.")


import json
import re
from pathlib import Path



def reformat_topic_subtopic_response():
    file_path_response = resource_path('topic_subtopic_response.json')
    with open(file_path_response, 'r', encoding='utf-8') as file:
        data = json.load(file)

    response_text = ""
    if isinstance(data.get("response"), list):
        for item in data["response"]:
            if isinstance(item, dict) and "text" in item:
                response_text += item["text"] + "\n\n"
            elif isinstance(item, str):
                response_text += item + "\n\n"
        response_text = response_text.strip()
    elif isinstance(data.get("response"), str):
        response_text = data["response"].strip()

    # Remove any leading text that is not part of the structured outline
    match = re.search(r'(\d+\.\s*.+)', response_text, re.DOTALL)
    if match:
        response_text = match.group(1).strip()

    # Split the response into individual topic lines using double newline
    lines = response_text.split("\n\n")
    formatted_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Match pattern: number. title: [subtopics]
        pattern = r'^(\d+\.)\s*(.+?)\s*:\s*(\[.*\])$'
        m = re.match(pattern, line)
        if m:
            number = m.group(1).strip()
            title = m.group(2).strip().upper()
            subtopics = m.group(3).strip()
            formatted_line = f"{number} {title}: {subtopics}"
            formatted_lines.append(formatted_line)
        else:
            formatted_lines.append(line)

    new_response = "\n\n".join(formatted_lines)

    new_data = {
        "number_of_topics": data.get("number_of_topics", ""),
        "number_of_subtopics": data.get("number_of_subtopics", ""),
        "response": new_response
    }

    with open(file_path_response, 'w', encoding='utf-8') as file:
        json.dump(new_data, file, indent=4)

if __name__ == '__main__':
    reformat_topic_subtopic_response()


if __name__ == '__main__':
    reformat_topic_subtopic_response()




import os
from pathlib import Path

def clean_topic_prompt_response1(generated_text):
    file_path = resource_path("topic_subtopic_response.txt")
    
    try:
        # Convert generated_text to string if it's not already a string
        if not isinstance(generated_text, str):
            generated_text = ''.join(map(str, generated_text)) if isinstance(generated_text, list) else str(generated_text)
        
        # Ensure the directory for the file exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Write the generated text to the file (header removed)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(generated_text)
           
            print(file_path)
        
        return file_path
    except Exception as e:
        raise Exception(f"Error saving file: {str(e)}")






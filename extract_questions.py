import docx2txt
import os
        
import shutil

import json
import re

from common_functions import resource_path, get_config_value, set_config_value
from MCQ import MCQ
from FILL_IN_GAP import *
from RMS import efficient_question_deduplication

def delete_file(file_path):
    file_path = resource_path(file_path)
    try:
        os.remove(file_path)
        print(f"The file {file_path} has been successfully deleted.")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except PermissionError:
        print(f"Permission denied: Unable to delete {file_path}.")
    except Exception as e:
        print(f"An error occurred while trying to delete {file_path}: {str(e)}")
        


def copy_questions_file():
    source_file = resource_path('questions.txt')
    destination_file = 'MCQ_RAW.txt'
    delete_file("MCQ_RAW.txt")

    try:
        # Copy the file
        shutil.copy2(source_file, destination_file)
        print(f"Successfully copied '{source_file}' to '{destination_file}'")
    except FileNotFoundError:
        print(f"Error: The file '{source_file}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied. Unable to create or write to '{destination_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function

def remove_section_b():
    file_path = resource_path('MCQ_RAW.txt')
    with open(file_path, 'r') as file:
        lines = file.readlines()

    section_b_index = None
    for i, line in enumerate(lines):
        if "SECTION B" in line:
            section_b_index = i
            break

    if section_b_index is not None:
        modified_content = lines[:section_b_index]
    else:
        modified_content = lines

    with open(file_path, 'w') as file:
        file.writelines(modified_content)
        
        
        
        
        

def convert_doc_to_txt(file_path):
    # Extract text from the .docx file
    delete_file("questions.txt")
    delete_file("MCQ_RAW.json")
    delete_file("FILL_IN_GAP_RAW.json")
  
    text = docx2txt.process(file_path)
    
    # Define the output path in the root directory
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "questions.txt")
    
    # Write the extracted text to questions.txt
    with open(output_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)
        
        
    
    copy_questions_file()    
    remove_section_b()
    MCQ()
    fill_in_gap()
    efficient_question_deduplication()


    
    print("\033[H\033[J")
    # print(questions)
    


    









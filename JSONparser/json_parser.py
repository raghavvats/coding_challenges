import json
import os
import glob
import re


# BROKEN & NOT IN USE
def load_all_json():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_files = glob.glob(os.path.join(base_dir, '**/*.json'), recursive=True)
    
    test_files = []
    for json_file in json_files:
        try:
            with open(json_file, 'r') as json_file:
                test_files.append(json.dumps(json_file))
        except FileNotFoundError:
            print(f"Error: {str(json_file)} does not exist")
    return test_files

def load_test_file(step_number):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    step_x_folder = os.path.join(current_directory, "tests", f"step{step_number}")
    step_x_files = os.listdir(step_x_folder)

    files = []
    for file_name in step_x_files:
        if file_name.endswith('.json'):
            file_path = os.path.join(step_x_folder, file_name)

            with open(file_path, 'rb') as raw_file:
                raw_data = raw_file.read()
                text = raw_data.decode('utf-8', errors='ignore')
                files.append(text)
    return files

def tokenize_and_label(json_string):
    tokens = re.findall(r'\w+|[{"\':}]', json_string)
    for i in range(len(tokens)):
        if len(tokens[i]) > 1 and tokens[i + 2] == ":" and len(tokens[i + 4]) > 1:
            tokens[i] = "KEY"
            tokens[i + 4] = "VALUE"
            i = i + 4
    return tokens

def validate_json(processed_json):
    return 0
    is_open = False

    for token in processed_json:
        if c == "{":
            is_open = True
        elif c == "}":
            is_open = False
    if is_open:
        return 1


data = load_test_file(2)
for file in data:
    processed_data = tokenize_and_label(file)
    print(processed_data)
    rv = validate_json(processed_data)
    if rv:
        print("Invalid. Return Code: ", rv)
    else:
        print("Valid.")


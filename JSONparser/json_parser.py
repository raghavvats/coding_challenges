import json
import os
import glob

def load_all_json(folder):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    test_folder = os.path.join(base_dir, folder)

    json_files = glob.glob(os.path.join(base_dir, '**/*.json'), recursive=True)
    
    test_files = []
    for json_file in json_files:
        try:
            with open(json_file, 'r') as json_file:
                test_files.append(json.dumps(json_file))
        except FileNotFoundError:
            print(f"Error: {str(json_file)} does not exist")
    return test_files

def validate_json(data):
    
    return 0

folder_name = input("test folder name: ")
all_json_data = load_all_json(folder_name)



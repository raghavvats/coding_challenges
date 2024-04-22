import json

def load_json(filename):
    try:
        with open(filename, 'r') as json_file:
            json_data = json.load(json_file)
            return json_data
    except FileNotFoundError:
        print(f"Error: {filename} does not exist")


file_name = input("file name: ")
json_data = load_json(file_name)

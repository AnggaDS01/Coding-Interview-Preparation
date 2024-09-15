import json

def read_json_recursively(data):
    if isinstance(data, dict):
        for key, value in data.items():
            read_json_recursively(value)
            result = f'Value: {value}'
            if not isinstance(value, (list, dict)):
                print(result)
    elif isinstance(data, list):
        for value in data:
            read_json_recursively(value)

with open('6.1. Algorithm/write_python_recursively_read_JSON/data/file.json', 'r') as file:
    file_json = json.load(file)

read_json_recursively(file_json)
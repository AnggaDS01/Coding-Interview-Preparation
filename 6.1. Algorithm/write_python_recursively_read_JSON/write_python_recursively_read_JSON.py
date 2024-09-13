import json

'''
This function reads a JSON object recursively and returns a list of strings representing the key-value pairs. It handles three cases:

1. If the data is a dictionary, it iterates over the key-value pairs, creates a string for each pair, and recursively calls itself for each value.
2. If the data is a list, it recursively calls itself for each item in the list.
3. If the data is neither a dictionary nor a list, it creates a string representing the value and adds it to the results.

The function also prints each key-value pair or value as it processes them.
'''

def read_json_recursively(data):
    """
    Recursively reads a JSON object and returns a list of strings representing the key-value pairs.

    Args:
        data (dict or list): The JSON object to be read.

    Returns:
        list: A list of strings, where each string represents a key-value pair in the JSON object.
    """
    results = []
    if isinstance(data, dict):
        for key, value in data.items():
            result = f"Key: {key}, Value: {value}"
            results.append(result)
            results.extend(read_json_recursively(value))
            print(result)
    elif isinstance(data, list):
        for value in data:
            read_json_recursively(value)
            results.extend(read_json_recursively(value))
    else:
        result = f"Value: {data}"
        results.append(result)
        print(result)

    return results

with open('./data/file.json', 'r') as file:
    file_json = json.load(file)

results = read_json_recursively(file_json)

print(results)
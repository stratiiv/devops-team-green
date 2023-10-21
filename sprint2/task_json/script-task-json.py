import json
import os
from argparse import ArgumentParser

def check_key(file_path):
    try:  # check if json file exists and is valid
        with open(file_path, 'r') as json_log:
            data = json.load(json_log)
            return data
    except FileNotFoundError:
        print("Error: file not found")
        return 1
    except json.JSONDecodeError:
        print("Error: file cannot be processed")
        return 2

def extract_values(obj, key):
    arr = []
    def extract(obj, arr, key):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results

parser = ArgumentParser()
parser.add_argument('f', help='path to json file')
parser.add_argument('k', help='key to find in json file')
arguments = parser.parse_args()
file_path = arguments.f
keyword = arguments.k
result = extract_values(check_key(file_path), keyword)
print(*result, sep='\n')

import json
import os
from argparse import ArgumentParser

def check_key(file_path, key):
    try:#check if json file exists and is valid
        with open(file_path, 'r') as json_log:
            data = json.load(json_log)
            if key in data:
                return data[key]
            else:
                return None
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None


parser = ArgumentParser()
parser.add_argument('f', help='path to json file')
parser.add_argument('k', help='key to find in json file')
arguments = parser.parse_args()
file_path = arguments.f
key = arguments.k
result = check_key(file_path, key)

if result is not None:
    print(f"The value for key '{key}' is: {result}")
else:
    print(f"The key '{key}' does not exist in the file or the file could not be processed")
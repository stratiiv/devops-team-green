
import json
import os
from argparse import ArgumentParser

def check_key(file_path, keyword):
    try: #check if json file exists and is valid
        with open(file_path, 'r') as json_log:
            data = json.load(json_log)
            #elements = []
            for case in data['accounts']:
                if keyword in case:
                    print(f"The value for key '{keyword}' #is: {case[keyword]}")
                else:
                    print(f"The key '{keyword}' does not exist in the file")
                    return None
    except FileNotFoundError:
        print("Error: file not found")
        return 1
    except json.JSONDecodeError:
        print("Error: file cannot be processed")
        return 2


parser = ArgumentParser()
parser.add_argument('f', help='path to json file')
parser.add_argument('k', help='key to find in json file')
arguments = parser.parse_args()
file_path = arguments.f
keyword = arguments.k
result = check_key(file_path, keyword)
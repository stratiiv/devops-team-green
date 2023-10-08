import sys
import yaml

def search_key_in_yaml(yml_file, key):
    try:
        with open(yml_file, 'r') as file:
            data = yaml.safe_load(file)
            values = []
            search_key_recursive(key, data, values)
            if values:
                return values
            else:
                return f"No values found for key '{key}' in the YAML file."
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{yml_file}' not found.")
    except yaml.YAMLError as e:
        raise ValueError(f"Error: Invalid YAML format in '{yml_file}': {e}")

def search_key_recursive(key, data, values):
    if isinstance(data, dict):
        for k, v in data.items():
            if k == key:
                values.append(v)
            search_key_recursive(key, v, values)
    elif isinstance(data, list):
        for item in data:
            search_key_recursive(key, item, values)

if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            raise ValueError("Error: Invalid number of arguments. Usage: python script.py <yml_file> <key>")
        
        yml_file = sys.argv[1]
        key = sys.argv[2]
        
        results = search_key_in_yaml(yml_file, key)
        if isinstance(results, list):
            for value in results:
                print(value)
        else:
            print(results)
    except Exception as e:
        print(e)

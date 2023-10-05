# https://docs.fileformat.com/programming/toml/
import sys


def find_password_in_toml(file_path):
    with open(file_path, 'r', encoding="utf8") as tomlfile:
        all_lines = ''
        for line in tomlfile:
            if 'password' in line.lower():
                all_lines = all_lines + line
    return all_lines


if __name__ == '__main__':
    try:
        # Check for the presence of command-line arguments
        if len(sys.argv) != 2:
            print(f"Usage: python find_password_toml.py <toml file path>  ")
            sys.exit(1)

        # Get command-line arguments
        file_toml_path = sys.argv[1]
        result = find_password_in_toml(file_toml_path)

        if result == '':
            print("Password not found in the TOML file.")
        else:
            print("Password was found in the TOML file. in such lines: \n", result)

    except Exception as e:
        print(str(e))

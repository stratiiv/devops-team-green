# https://docs.fileformat.com/programming/toml/
import sys


def find_password_in_toml(file_path):
    """
    Function To find Passwords. Works like its regular Text file
    :param file_path: Path to toml File
    :return: List with passwords
    """
    with open(file_path, 'r', encoding="utf8") as tomlfile:
        all_lines = []
        for line in tomlfile:
            if 'password' in line.lower():
                res = line.split('=')[-1].strip().strip('"')
                all_lines.append(res)
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

        if len(result) == 0:
            print("Password not found in the TOML file.")
        else:
            print("Password was found in the TOML file. in such lines: \n", result)

    except Exception as e:
        print(str(e))

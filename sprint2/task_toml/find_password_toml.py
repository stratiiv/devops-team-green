import sys
import toml


def find_password_in_toml(file_path):
    """
    Function To find Passwords. Works with library TOML
    :param file_path: Path to toml File
    :return: List with passwords
    """
    with open(file_path, 'r') as tomlfile:
        data, passwords = [toml.load(tomlfile)], []

        while data:
            dict_ = data.pop()
            for key, value in dict_.items():
                if 'password' in key.lower():
                    passwords.append(value)
                if isinstance(value, dict):
                    data.append(value)
        return passwords


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            print(f"Usage: python find_password_toml.py <toml file path>  ")
            sys.exit(1)

        file_toml_path = sys.argv[1]
        result = find_password_in_toml(file_toml_path)

        if len(result) == 0:
            print("Password not found in the TOML file.")
        else:
            print('\n'.join(result))
    except Exception as e:
        print(str(e))


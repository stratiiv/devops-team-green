import sys
import toml


def find_password_in_toml(file_path):
    with open(file_path, 'r') as tomlfile:
        data, passwords = [toml.load(tomlfile)], []
        while data:
            dict_ = data.pop()
            for key, value in dict_.items():
                if key.lower() == 'password':
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
            print("Password was found in the TOML file. in such key: \n", result)

    except Exception as e:
        print(str(e))

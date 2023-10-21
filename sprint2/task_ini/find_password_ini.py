import os
from configparser import ConfigParser
from argparse import ArgumentParser


def search_in_config(path: str, key: str) -> None:
    config = ConfigParser()
    config.read(path, encoding='utf-8')

    for section in config.sections():
        if value := config.get(section, key, fallback=None):
            print(value)


def main():
    parser = ArgumentParser(description='Search a value by key and return it.')
    parser.add_argument('path', help='The file with .ini extension to search in.')
    parser.add_argument('key', help='The key used to search.')
    arguments = parser.parse_args()

    path = arguments.path
    key = arguments.key

    if not os.path.isfile(path):
        print(f'{path} is directory or does not exist.')
        exit(1)

    if not path.endswith('.ini'):
        print(f'{path} is not an .ini file.')
        exit(1)

    search_in_config(path, key)


if __name__ == '__main__':
    main()

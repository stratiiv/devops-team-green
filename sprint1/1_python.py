import os
from argparse import ArgumentParser


# Define a custom exception class for when a path does not exist
class PathDoesNotExists(Exception):
    """Path does not exist."""

    def __init__(self, path):
        self.path = path

    def __str__(self):
        return f'{self.path} does not exist.'


def main():
    # Create an ArgumentParser object to handle command-line arguments
    parser = ArgumentParser(description='Search for files with specified extension.')

    # Define two required command-line arguments: 'path' and 'extension'
    parser.add_argument('path', help='The directory to search in.')
    parser.add_argument('extension', help='The extension to search files with.')

    arguments = parser.parse_args()

    path = arguments.path
    extension = arguments.extension

    # Check if the specified 'path' is a directory; if not, raise the custom exception
    if not os.path.isdir(path):
        raise PathDoesNotExists(path)

    files_list = next(os.walk(path))[2]

    found_files = []

    for file in files_list:
        if file.endswith(extension):
            found_files.append(file)

    if found_files:
        print(f'Files with matches in {os.getcwd()}:', *found_files, sep='\n')
    else:
        print('No such files.')


if __name__ == '__main__':
    try:
        main()
    except PathDoesNotExists as e:
        print(e)

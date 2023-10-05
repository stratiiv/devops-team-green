from argparse import ArgumentParser
import os
from pathlib import Path
from typing import List


def find_files_with_text(directory: str, text: str) -> List[str]:
    """
    Search for text in .txt files within a directory.
    """
    matching_files = []
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            filename = os.path.join(subdir, file)
            if Path(filename).suffix == '.txt':
                with open(filename, encoding='utf8', errors='ignore') as f:
                    if text in f.read():
                        matching_files.append(filename)
    return matching_files


def main():
    parser = ArgumentParser(description='Search for text in .txt files within a directory.')
    parser.add_argument('path', help='The directory to search in')
    parser.add_argument('string', help='The text to search for in .txt files')
    args = parser.parse_args()

    path = args.path
    text = args.string

    if not os.path.exists(path) or not os.path.isdir(path):
        print(f'Error! {path} is not a valid directory')
        return

    result = find_files_with_text(path, text)

    if not result:
        print(f"No files containing the specified text in {path}")
    else:
        print("Files containing the specified text:")
        for file_path in result:
            print(file_path)


if __name__ == '__main__':
    main()

import os
import sys


def count_files_with_ext(dir: str, ext: str) -> int:
    """
    Function to count number of files with extension
    :param dir: Target Directory where to search
    :param ext: Extension of File
    :return: Count files
    """
    count = len([f for f in os.listdir(dir) if f.endswith(f'.{ext}')])
    return count


if __name__ == '__main__':
    try:
        if len(sys.argv) != 3:
            print("Usage: python script.py <directory path> <extension>")
            sys.exit(1)

        directory = sys.argv[1]
        extension = sys.argv[2]
        if not os.path.exists(directory):
            raise FileNotFoundError(f'Directory "{directory}" not found.')
        result = count_files_with_ext(directory, extension)

        if isinstance(result, int):
            print(result)
        else:
            print(f'Error: {result}')
    except Exception as e:
        print(str(e))

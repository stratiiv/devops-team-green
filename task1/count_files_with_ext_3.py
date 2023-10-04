import os
import sys


def count_files_with_ext(directory, extension):
    try:
        count = 0
        # Check if the directory exists
        if not os.path.exists(directory):
            raise FileNotFoundError(f'Directory "{directory}" not found.')

        # Iterate through all files in the directory
        for filename in os.listdir(directory):
            if filename.endswith(f'.{extension}'):
                count += 1

        return count
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    # Check for the presence of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory path> <extension>")
        sys.exit(1)

    # Get command-line arguments
    directory = sys.argv[1]
    extension = sys.argv[2]

    # Call the function to count files
    result = count_files_with_ext(directory, extension)

    if isinstance(result, int):
        print(f'Number of files with the .{extension} extension in the directory {directory}: {result}')
    else:
        print(f'Error: {result}')

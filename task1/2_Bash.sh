#!/bin/bash

# check arguments
if [ "$#" -ne 2 ]; then
    echo "Error: Enter path and text as arguments."
    exit 1
fi

# check text or number
if [[ "$2" =~ ^[0-9]+$ ]]; then
    echo "Error: Second argument must be a text."
    exit 1
fi

# check directory
if [ ! -d "$1" ]; then
    echo "Error: Path doesn't exist or it's not a directory."
    exit 1
fi

# search files directory
files_with_text=$(grep -rl "$2" "$1")

# show files
if [ -z "$files_with_text" ]; then
    echo "No files with this text."
else
    echo "Files with text in directory:"
    echo "$files_with_text"
fi
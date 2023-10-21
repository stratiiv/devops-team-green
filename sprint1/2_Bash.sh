#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Error: Enter path and text as arguments."
    exit 1
fi

if [[ "$2" =~ ^[0-9]+$ ]]; then
    echo "Error: Second argument must be a text."
    exit 1
fi

if [ ! -d "$1" ]; then
    echo "Error: Path doesn't exist or it's not a directory."
    exit 1
fi

files_with_text=$(grep -rl "$2" "$1")

if [ -z "$files_with_text" ]; then
    echo "No files with this text."
else
    echo "Files with text in directory:"
    echo "$files_with_text"
fi
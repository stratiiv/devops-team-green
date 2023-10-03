#!/bin/bash

# Check if the number of command-line arguments is proper
if [ $# -ne 2 ]; then
    echo "Usage: $0 <path> <extension>"
    exit 1
fi

dir="$1"
ext="$2"

# Check if the provided directory path does not exist
if [ ! -d "$dir" ]; then
    echo "No such directory"
    exit 1
fi

# Change the current working directory to the provided directory path or exit if unsuccessful
cd "$dir" || exit 1

# Use the 'find' command to search for files with the specified extension in the current directory and its subdirectories
find . -type f -name "*$ext" -print

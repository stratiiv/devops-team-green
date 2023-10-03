#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: $0 <path> <extention>"
    exit 1
fi

dir="$1"
ext="$2"

if [ ! -d "$dir" ]; then
    echo "No such a directory"
    exit 1
fi

cd "$dir" || exit 1
find . -type f -name "*$ext" -print
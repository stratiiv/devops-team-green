#!/bin/bash
usage() {
  echo "Usage: $0 -p <path> -s <search_string>"
  exit 1
}

while getopts "p:s:" opt; do
case "$opt" in
    p) path="$OPTARG";;
    s) search_string="$OPTARG";;
    *) usage;;
esac
done

if [ -z "$path" ] || [ -z "$search_string" ]; then
    usage
fi

found_files=$(grep -rl "$search_string" "$path")

if [ -z "$found_files" ]; then
  echo "No files found containing '$search_string' in '$path'."
else
  echo "Files containing '$search_string' in '$path':"
  echo "$found_files"
fi
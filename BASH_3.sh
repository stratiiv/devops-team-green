#!/bin/bash
if [ "$#" -eq 2 ]; then
	aPath="$1"
	aExt="$2"
else
	echo "Error; args PATH and EXTENTION are necessary"
	exit 1
fi

if[! -d "$aPath"] then
	echo "directory '$aPath' does not exists"
	exit 1
fi

fCount=$(find "$aPath" -name "*.$aExt" | wc -l)
echo "there is '$fCount' *.'$aExt' files in '$aPath'"
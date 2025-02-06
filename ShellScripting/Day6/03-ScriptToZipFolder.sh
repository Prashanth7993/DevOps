#!/bin/bash
#Author: Prashanth
#Purpose: A Shell Script file to zip a folder.
# shellcheck disable=SC2113
#Usage: ./03-ScriptToZipFolder.sh

echo "Enter the Folder Name To Zip"
read -r file
zip -r Newfolder1.zip "$file"
if [ $? -eq 0 ]; then
    echo "Folder zip created"
else
    echo "Folder zip not created"
fi



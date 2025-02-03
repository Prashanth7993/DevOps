#!/bin/sh
#Author: Prashanth
#Purpose: Creating a backup file
# shellcheck disable=SC2113
#Usage: ./06-CreatingBackupFile.sh


echo "Enter the file"
read -r File
echo "Enter the path"
read -r Path

cp "$File" "$Path"
echo "Backup Complted"



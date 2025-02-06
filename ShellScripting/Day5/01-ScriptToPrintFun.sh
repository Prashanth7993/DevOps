#!/bin/bash
#Author: Prashanth
#Purpose: A Shell Script file to print file.
#Usage: ./01-SciptToPrintFun.sh

print_size(){
    local directory="$1"
    local size=0
    local du_out=0
    # du_out=$(du -h)
    size=$(ls -lh "$directory" | awk 'NR==1 {print $2}')

    echo "message passed: $size"
    echo "disk usage: $du_out"
}
echo "enter the message you want to print"
read -r message
print_size "$directory"
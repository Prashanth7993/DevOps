#!/bin/sh
#Author: Prashanth
#Purpose: Converting Lower to upper
# shellcheck disable=SC2113
#Usage: ./01-ConvertLowerUpper.sh

echo "Enter the String: "
read -r Str
myvarlen=${#Str}
rev=""
for(( i=$myvarlen-1; i>=0; i-- )); do
    rev="$rev${Str:i:1}"
done
if [ $Str == $rev ]; then
    echo "It is a palindrome"
else
    echo  "It is not a palindrome"
fi
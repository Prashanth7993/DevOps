#!/bin/sh
#Author: Prashanth
#Purpose: Converting Lower to upper
# shellcheck disable=SC2113
#Usage: ./01-ConvertLowerUpper.sh

echo "Enter the String: "
read -r Str

echo " $Str " | tr '[:lower:]' '[:upper:]'
 



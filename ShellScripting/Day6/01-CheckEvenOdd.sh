#!/bin/bash
#Author: Prashanth
#Purpose: A Shell Script file to check even or odd.
# shellcheck disable=SC2113
#Usage: ./02-CheckEvenOdd.sh


echo "Enter tne number: "
read -r num

if [ $((num%2)) -eq 0 ]; then
    echo "Even number"
else
    echo "Not a Even number"
fi
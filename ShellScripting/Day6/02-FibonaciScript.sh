#!/bin/bash
#Author: Prashanth
#Purpose: A Shell Script file Fibonacci Series
# shellcheck disable=SC2113
#Usage: ./02-FibonaciScript.sh

# 0 1 1 2 3 5 8 13 21 34 55 89

echo "Enter the number you want: "
read -r num

a=0
b=1

for(( i=2; i<$num; i++ )); do
    next=$((a+b))
    a=$b
    b=$next
    echo "$next"
done
echo 


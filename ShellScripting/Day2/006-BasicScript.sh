#!/bin/bash
#Author :SB
#Purpose: Basic Scirpt 
#usage: ./006-BasicScript.sh
 
echo "please enter the number"
read -r no
 
if [[ $no -le 20 ]]; then
    echo "more score needed"
elif [[ $no -gt 20 && $no -le 40 ]]; then
    echo "average score"
else
    echo "excellent"
fi
 
for i in 1 2 3 4 5
do
    echo "$i"
done
 
for i in {1..5};
do
    echo "$1"
done
 
for i in $(seq 1 5);
do
    echo "$i"
done
 
for (( i=1; i<10; i++));
do
    echo "$i"
done

echo "all arguments combined together $*"
echo "no. of arguments $#"
echo "first $1"
echo "expands all the command line on separate words $@"
echo "ProcessId of the current process $$"
 
sleep 400 &
echo "ProcessId of the recently background process $!"
echo "file name of the current programm $0"


set -x
set `date`
echo "Today is $1"
echo "Month is $2"
echo "Date is $3"
echo "Year is $4"
echo "Time is $5"
echo "AM/PM is $6"
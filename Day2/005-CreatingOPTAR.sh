#!/bin/sh
#Author: Prashanth
#Purpose: Creating OPTAR with getops
# shellcheck disable=SC2113
#Usage: ./005-CreatingOPTAR.sh

while getops a:b: flag;do
    case $flag in
    a) ab=$OPTARG;;
    b) bc=$OPTARG;;
    ?) echo "I Don't Understand this value"
    esac
done
echo "first value $ab, secound value $bs"
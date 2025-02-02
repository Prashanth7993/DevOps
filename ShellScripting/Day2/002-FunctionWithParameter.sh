#!/bin/sh
#Author: Prashanth
#Purpose: Learning function with parameter
# shellcheck disable=SC2113
#Usage: ./002-FunctionWithParameter.sh

function sum {
    local total=$(( $1 + $2 ))
    echo "$total" 
}
result=$(sum 5 9)
echo " the result is $result"
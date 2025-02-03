#!/bin/bash
#Author :SB
#Purpose:Learning function with parameter
#usage: ./demoProj.sh
 
echo "Enter the number of Physics"
read -r pM
echo "Enter the number of Chemistry"
read -r cM
echo "Enter the number of Math"
read -r mM
 
if [ "$pM" -lt 35 ] || [ "$cM" -lt 35 ] || [ "$mM" -lt 35 ]; then
    echo "Sorry, You have failed"
else
    tm=$((pM + cM + mM))
    avgM=$((tm / 3))
   
    if [[ "$avgM" -gt 80 ]]; then
        echo "Excellent and average is $avgM"
    elif [[ "$avgM" -gt 60 ]]; then
        echo "First Class and average is $avgM"
    elif [[ "$avgM" -gt 45 ]]; then
        echo "Second Class and average is $avgM"
    fi
fi
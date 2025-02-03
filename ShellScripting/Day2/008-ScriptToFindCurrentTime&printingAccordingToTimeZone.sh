#!/bin/bash
#Author :SB
#Purpose:ScriptToFindCurrentTime&printingAccordingToTimeZone
#usage: ./008-ScriptToFindCurrentTime&printingAccordingToTimeZone.sh

echo "Please enter the time"
read -r no
 
current_hour=$(date +%H)
 
if [[ $current_hour -gt 0  && $current_hour -lt 12 ]]; then
    echo "Good MORNING"
elif [[ $current_hour -gt 12 && $current_hour -lt 16 ]]; then
    echo "Good Afternoon"
elif [[ $current_hour -gt 16 && $current_hour -lt 20 ]]; then
    echo "Good Evening"
elif [[ $current_hour -gt 20 && $current_hour -lt 24 ]]; then
    echo "Good Night"
fi
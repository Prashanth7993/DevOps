#!/bin/bash
#Author: Prashanth
#Purpose: A Shell Script file to print hardware info file.
# shellcheck disable=SC2113
#Usage: ./02-ScriptToPrintHardwareInfo.sh

cpuinfo=$(lscpu)
echo "Cpu Details $cpuinfo"

hwinfo=$(lshw)
echo "Hardware details $hwinfo"

exe=$(free -h)
echo "free command $exe"

uname=$(uname -a)
echo "uname command $uname"

meminfo=$(sudo cat /proc/meminfo)
echo "meminfo command $meminfo"

disk=$(lsblk)
echo "diskinfo command $disk"


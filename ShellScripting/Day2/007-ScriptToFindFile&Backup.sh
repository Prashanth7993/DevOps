#!/bin/bash
#Author :SB
#Purpose:Finding file and giving backup
#usage: ./007-ScriptToFindFile&Backup.sh
 
function backup {
    echo "Enter the the file name"
    read -r mf
    if [ -f $mf ]; then
        echo "file exists"
        cp $mf /tmp/test.sh
    else    
        echo "file not found"
    fi
    if [ $? -ne 0 ]; then
        echo "backup failed $?"
    fi
}
backup
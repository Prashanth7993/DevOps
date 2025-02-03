#!/bin/sh
#Author: Prashanth
#Purpose: ExtractGmailInTexFile
# shellcheck disable=SC2113
#Usage: ./05-ExtractGmailInTexFile.sh



# Check if filename is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

# Extract Gmail addresses from the file
grep -o '[a-zA-Z0-9._%+-]\+@gmail\.com' "$1" > extracted_gmails.txt

# Display the extracted emails
echo "Extracted Gmail addresses:"
cat extracted_gmails.txt

#Note: The -o option in grep is used to only print the matching part of a line instead of the entire line.


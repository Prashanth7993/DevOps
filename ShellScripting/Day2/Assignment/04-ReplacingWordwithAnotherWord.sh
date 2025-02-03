#!/bin/sh
#Author: Prashanth
#Purpose: ReplacingWordwithAnotherWordg
# shellcheck disable=SC2113
#Usage: ./04-ReplacingWordwithAnotherWord.sh

echo "Hi Prashanth" | sed "s/Hi/J/g"
#Output: J Prashanth
#Note: Usign Sed we can Replace Entire Word with one letter.
# Breakdown of s/hello/h/g
# s → Stands for substitute (used for find and replace).
# hello → The word you want to find.
# h → The replacement for hello.
# g → Stands for global, meaning it will replace all occurrences in the line.

echo "Hi Prashanth" | tr "Hi" "J"
#Output: JJ Prashanth

#Note: Usign tr we can Replace Each character in word.


echo "Hello123@ World!456" | tr -cd 'A-Za-z '

# The -cd option in the tr command is a combination of two flags:
# -c (complement) → Inverts the character set, meaning it selects all characters except those specified.
# -d (delete) → Deletes the selected characters.

echo "Hello123@ World!456" | tr -d '0-9!@#$%^&* '
#Note:It will delet the word or letters or Number given by you

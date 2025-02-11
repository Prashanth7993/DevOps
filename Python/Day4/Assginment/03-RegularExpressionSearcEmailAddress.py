#Implement a regular expression to search for email addresses in a text file

import re
import os
File = input("Enter the file name or path :")
f = open(File)
pattern = '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,4}' 
ls=[]
def SearchFileGmail(File):
    for i in f.readlines():
        match = re.findall(pattern,i)
        if match:
            ls.append(match)
    
    for i in ls:
        print(i)

SearchFileGmail(File)
    


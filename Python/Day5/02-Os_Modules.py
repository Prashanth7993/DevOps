import os
try:
    print("Current working directory : ",os.getcwd())
    # f = open("file.txt")
    #print(f.readline())
    # print(type(f.readlines()))
    # print(type(f.readline()))
    #print(f.read())
    # os.remove("file.txt")
    # print("file deleted")
except:
    print("problem in file not found")
finally:
    # f.close()
    print("closing")
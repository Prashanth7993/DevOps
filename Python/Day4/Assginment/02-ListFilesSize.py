

#Use the os module to list all files in a directory and display their sizes.
import os
try:
    def listFileSize(directory):
        if os.path.exists(directory):
            for filename in os.listdir(directory):
                file_path = os.path.join(directory,filename)
                if os.path.isfile(file_path):
                    print(f"filename {filename} - {os.path.getsize(file_path)}bytes")
        else:
            print("Directory is not found")
except:
    print("Script has some problem")

directory = input("Enter the file directory :")
listFileSize(directory)

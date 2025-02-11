import os
import time
def create_files(directory, file_names):
    if not os.path.exists(directory):
        # os.makedirs(directory)
        os.mkdir(directory)
    for file_name in file_names:
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'w') as file:
            file.write("This is a sample file: " + file_name)
        print(f"Created: {file_path}")

def delete_files(directory, file_names, delay):
    time.sleep(delay)
    for file_name in file_names:
        file_path = os.path.join(directory, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        else:
            print(f"File not found: {file_path}")

directory = input("Enter Directory Path")
file_names = list(map(str,input("Enter file names to create and delete").split(" ")))
delay = 10  
create_files(directory, file_names)
delete_files(directory, file_names, delay)
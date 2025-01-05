import os

# Specify the directory path
directory_path = '/'

# Use os.listdir() to get the list of files and directories
try:
    with os.scandir(directory_path) as entries:
        for entry in entries:
            print(entry.name)
except FileNotFoundError:
    print("Directory not found")
except PermissionError:
    print("You do not have permission to access this directory")
except Exception as e:
    print(f"An error occurred: {e}")


# 5. Label the program written in problem 4 with comments. 

import os

# Specify the directory you want to list
directory_path = '/'

# List all files and directories in the specified directory
for item in os.listdir(directory_path):
    print(item)
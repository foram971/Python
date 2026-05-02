#Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that. 

import os

# List directory contents
for item in os.listdir():
    print(item)
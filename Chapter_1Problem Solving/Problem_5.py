# Label the program written in problem 4 with comments. 
import os

# Get current working directory
current_directory = os.getcwd()
print(f'Current Directory: {current_directory}\n')

# List items in the directory
print('Directory contents:')
for item in os.listdir(current_directory):
    print(item)
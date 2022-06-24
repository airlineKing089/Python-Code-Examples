# user choices example

import time
import sys

def QuitProgram():
    print("Exiting...")
    time.sleep(0.5)
    sys.exit()

possible_choices = ['1', '2', '3', '4']

user_choices = """What would you like to do?
[1] Option 1
[2] Option 2
[3] Option 3
[4] Exit Program"""

print(user_choices)
option = input("Your Choice: ")

if option not in possible_choices:
    print("Invalid Option...")
    time.sleep(0.5)
    QuitProgram()
elif option == '1':
    pass
elif option == '2':
    pass
elif option == '3':
    pass
else:
    QuitProgram()
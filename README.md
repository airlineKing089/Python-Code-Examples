# Python-Code-Examples
Python-Code-Examples consists of many (in the future) short examples of simplistic things for people learning python. Each example will becommented so you know how it works. These will cover both simple and semi-complex topics.

## Info
- All code was made by me, no-one else
- These examples are made in idle, the Python development IDE which comes pre-installed with Python
- Link to [Python](https://www.python.org/)

## Examples
Each example below is explained with what it does and how it works

### Example 1 - user_choices
This script gets user input to decide what the user wants to do and has error detection.

Code:
```python
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
```

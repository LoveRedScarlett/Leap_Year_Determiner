# -*- coding: utf-8 -*-
"""ScarMaxwellAssignment5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pMUyiLAsNy9g3t2ncH-z0Gwn4vNKyrmg
"""

## Scar Maxwell 2/3/24

print("This program will tell you if the year you enter is a leap year.")
year = input("Please enter a year: ") # declaring year variable with user input

year = int(year) # User inputs needs to be converted into a integer

if year % 100 == 0 and year % 400 == 0 : # Determines if the year entered is perfectly divisible by 100 and 400.
  print(year, "is a leap year!")
elif year % 4 == 0 and year % 100 != 0: # Determines if the year is not divisible perfectly by 100 but is divisible by 4.
  print(year, "is a leap year!")
else:
  print(year, "is not a leap year!")
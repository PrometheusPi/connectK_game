"""
This game is inspired by a job interview test reported by Johannes Pausch.

You have a (infinitly - here finite) horizontal field and try to connect k points.
Each player takes turns to add their stones. In contrast to classical connect-4, stones are added beneeth existing stones and push up the stones of the collumn.
"""

import os
import time

#print('Coding Ninjas!\n'*5)

#time.sleep(5)

#os.system('clear')

import sys

def clean_screen():
    """
    clean terminal screen
    """
    sys.stdout.write("\33[H\33[2J") #"\33" is the ESC character
    sys.stdout.flush()

for step in range(100):
    for i in range(5):
        print("\n")
    print("x"*step)
    print("\n")
    for i in range(5):
        print("\n")
    time.sleep(0.2)
    clean_screen()
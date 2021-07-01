from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should be
able to solve the "repair the quad" problem from Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter code.

Your next task is to repair the damage done to the Stanford Main Quad in the 1989 Loma Prieta earthquake. In particular, Karel should repair a set of arches where some of the stones (represented by beepers, of course) are missing from the columns supporting the arches, as illustrated in the figure below.


"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        piller_beeper()
    piller1_beeper()      

def filling_beeper():
    if no_beepers_present():
        put_beeper()
    move()       
def turn_around():
    turn_left()
    turn_left()  
def move_again():
    move()
    move()
    move()
    move()      
def piller_beeper():
    turn_left()
    while front_is_clear():
         filling_beeper()
    if no_beepers_present():
        put_beeper()     
    turn_around()
    while front_is_clear():
        move()
    turn_left() 
    move_again()
def piller1_beeper():
    turn_left()
    while front_is_clear():
         filling_beeper()
    if no_beepers_present():
        put_beeper()     
    turn_around()
    while front_is_clear():
        move()
    turn_left() 

if __name__ == '__main__':
    run_karel_program('SampleQuad1.w')
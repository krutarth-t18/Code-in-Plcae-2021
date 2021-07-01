from karel.stanfordkarel import *

"""
File: RampClimbingKarel.py
--------------------
When you finish writing this file, RampClimbingKarel should be
able to draw a line with slope 1/2 in any odd sized world
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.

    The key to drawing a diagonal line with slope ½ is to move two steps forward and one step up between each beeper. In this problem you can and should assume that the world is an odd number of columns across. Solving the problem for even columns as well is much harder and would count as an "extension".

    You should assume
    Karel always begins at the bottom left corner of and empty world facing East.
    You may assume that the world is an odd number of columns across
    Karel's bag has infinite beepers.
    It does not matter which direction Karel ends up facing.
    The world is always square (the world's height is the same as its width)
    """
    while front_is_clear():
        ramp_climbing()
    put_beeper()    
def ramp_climbing():
    put_beeper()
    move()
    move()
    turn_left()
    move()
    turn_right()
def turn_right():
    turn_left()
    turn_left()
    turn_left()        

if __name__ == '__main__':
    run_karel_program('RampKarel1.w')
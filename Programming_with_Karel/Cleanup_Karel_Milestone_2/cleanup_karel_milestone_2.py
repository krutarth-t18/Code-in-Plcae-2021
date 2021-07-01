from karel.stanfordkarel import *

"""
File: CleanupKarel.py
--------------------
When you finish writing this file, CleanupKarel should be able to
pick up all beepers from the first row of any sized world and
end in the bottom right corner facing East.

Karel has a bit of spring cleaning to do! Karel's world will have 
beepers in some positions in the bottom row; write a program to 
have Karel walk across the bottom row and, at each position, 
pick up a beeper only if one is present. Notice that you've 
already written the code to check if a beeper is present and 
only pick up a beeper if one is there from the previous milestone 
-- you should use your code from the previous milestone as a helper 
function to help with the decomposition of this problem!

Additionally, note that Karel's starting position will never contain a beeper, so there's no need to check it.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        take_beeper()
    pick_beeper()    
def take_beeper():
    if beepers_present():
        pick_beeper()
    move()            

if __name__ == '__main__':
    run_karel_program('Cleanup1.w')
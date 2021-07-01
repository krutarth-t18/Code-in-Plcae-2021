from karel.stanfordkarel import *

"""
File: ExtensionKarel.py
-----------------------
This file is for optional extension programs. 
"""

def main():
    """
    I have written a code, which shows the heart of karel in the Checkerboard world. Here first I used
    the code of previous problem(the Midpoint) to find the midpint of the world. After that I divided
    the heart of karel in two parts one is left side's heart and right side's heart.
    """
    multi_spot() # this function can find the midpoint
    # when the code find midpoint then below function make a left side of heart
    karels_left_sides_heart()
    #then karel moves down for making right side of heart
    moving_to_make_right_sides_heart() 
    karels_right_sides_heart()# this function makes another side of heart 
    comming_to_origin() # and finally karel come to its initial poisition by this function
def comming_to_origin(): 
    move_to_wall()
    turn_left()
    move_to_wall()
    turn_left()    
def moving_to_make_right_sides_heart():
    turn_right()
    move_to_wall()
    turn_left()
    move()    

"""THE below FUNDTIONS ARE FOR karels_right_sides_heart()"""

def karels_right_sides_heart():
    putting_red_for_right_side()
def putting_red_for_right_side():
    paint_corner(RED)        
    move_to_upper_rightside_row()
    red_at_cros_right_line()
    moving_up_with_red_at_right()
    red_at_top_right_row()
def red_at_top_right_row():
    turn_left()
    move()
    while corner_color_is(BLANK):
        if corner_color_is(BLANK):
            paint_corner(RED)
            move() 
def moving_up_with_red_at_right(): #it will make a red vertical line to the right side's wall
    turn_left()
    move()
    while front_is_clear():
        paint_corner(RED)
        move()    
def red_at_cros_right_line(): #it will make the crossed red line from mdipoint to right side's wall
    while front_is_clear():
        move()
        turn_left()
        move()
        paint_corner(RED)
        turn_right()

def move_to_upper_rightside_row(): #this function goes to top side of the coloumn which is midpoint
    turn_left()
    move_to_wall()
    paint_corner(RED)
    turn_around()
    move()
    paint_corner(RED)
    move_to_wall()
    turn_left()

"""THE BELOW FUNDTIONS ARE FOR karels_left_sides_heart()"""

def karels_left_sides_heart(): 
    pick_beeper()
    putting_red_for_left_side()
def putting_red_for_left_side():
    paint_corner(RED)
    move_to_upper_leftside_row()
    red_at_cross_left_line()
    moving_up_with_red_at_left()
    red_at_top_left_row()
def move_to_upper_leftside_row(): #this function goes to top side of the coloumn which is midpoint
    turn_right()
    move_to_wall()
    paint_corner(RED)
    turn_around()
    move()
    paint_corner(RED)
    move_to_wall()
    turn_right()
def red_at_top_left_row(): 
        turn_right()
        move()
        while corner_color_is(BLANK):
            if corner_color_is(BLANK):
                paint_corner(RED)
                move()   
def moving_up_with_red_at_left(): #it will make a red vertical line to the left side's wall
    turn_right()
    move()
    while front_is_clear():
        paint_corner(RED)
        move()    
def red_at_cross_left_line(): #it will make the crossed red line from mdipoint to left side's wall 
    while front_is_clear():
        move()
        turn_right()
        move()
        paint_corner(RED)
        turn_left() 
"""THE ABOVE FUNDTIONS ARE FOR karels_left_sides_heart()"""    

"""THE BELOW FUNDTIONS ARE FOR FINDING THE MIDPOINT OF THE WORLD"""

def multi_spot(): #this function is for bigger than 1X1 world
    """ pre condition: facing east, position at bottom left hand side"""
    """ post conition: facing east, position at top right hand side""" 
    while front_is_clear(): 
        beepers_slop()
    turn_right()
    move_to_wall()
    finding_midpoint()
def finding_midpoint(): 
    turn_right()
    check_beeper()
def check_beeper(): #it will check at which centre position beeper have
    while no_beepers_present():
        move()            
        if no_beepers_present():
            turn_right()
            move()
            turn_left()
    if left_is_clear():
        putting_beeper_to_midpoint()
    if front_is_clear():
        removing_extra_beepers()    
def putting_beeper_to_midpoint(): #finally it puts the beeper to midpoint of bottom row
    turn_left()
    move_to_wall()
    put_beeper()   
    turn_right()

def removing_extra_beepers(): #at the send it will remove all extra beepers   
    move_to_wall()
    turn_around()
    removing_beeper()
    comming_to_midpoint()

def removing_beeper():
    while front_is_clear():
        pick_beeper()
        turn_left()
        move()
        turn_right()
        move() 

def comming_to_midpoint(): #by this karel will come to its final position        
    turn_right()
    move_to_wall()
    turn_right()
    while no_beepers_present():
        move()   

def beepers_slop(): #it will make a line of beepers from Left to Right hypotenuse 
    put_beeper()
    turn_left()
    move()
    turn_right()
    move()

"""THE ABOVE FUNDTIONS ARE FOR FINDING THE MIDPOINT OF THE WORLD"""

def move_to_wall():
    while front_is_clear():
        move()
def turn_around():
    turn_left()
    turn_left()
def turn_right():
    for i in range(3):
        turn_left()
if __name__ == "__main__":
    run_karel_program('Checkerboard')
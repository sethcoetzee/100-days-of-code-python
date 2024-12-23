# Day 6 Project: Escaping the Maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()
     
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else: 
        turn_left()

# Note: Comde is NOT complete. Will return after day 15 to fix.
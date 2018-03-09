think(0)
# Variables
def turn_right():
    repeat 3:
        turn_left()
def turn_around():
    repeat 2:
        turn_left()
def search():
    turn_left()
    if front_is_clear():
        move()
        turn_left()
        if front_is_clear():
            move()
            turn_left()
            if front_is_clear():
                repeat 2:
                    move()
                turn_around()
                build_wall()
                turn_left()
            else:
                turn_left()
                move()
                turn_right()
                move()
                turn_right()
                move()
                turn_around()
                build_wall()
                turn_left()
        else:
            turn_left()
            move()
            turn_right()
            move()
            if right_is_clear():
                turn_around()
                build_wall()
                turn_left()
            else:
                turn_left()
                move()
                turn_around()
                build_wall()
                turn_left()
    else:
        turn_left()
        move()
        if right_is_clear():
            turn_right()
            move()
            if right_is_clear():
                turn_around()
                move()
                turn_left()
                build_wall()
                turn_left()
            else:
                turn_around()
                repeat 2:
                    move()
                turn_around()
                build_wall()
                turn_left()
        else:
            turn_left()
            move()
            turn_around()
            build_wall()
            turn_left()
# CODE STARTS HERE
repeat 100:
    if right_is_clear():
        turn_right()
        move()
        if wall_on_right():
            pass
        else:
            turn_right()
            move()
            turn_left()
            if front_is_clear():
                move()
                turn_left()
                if front_is_clear():
                    move()
                    turn_left()
                    if front_is_clear():
                        move()
                        turn_around()
                        search()
                    else:
                        turn_left()
                        move()
                        turn_right()
                        move()
                        turn_right()
                        move()
                        turn_around()
                        build_wall()
                        turn_left()
                else:
                    turn_left()
                    move()
                    turn_right()
                    move()
                    if right_is_clear():
                        turn_around()
                        build_wall()
                        turn_left()
                    else:
                        turn_right()
                        search()
            else:
                turn_left()
                move()
                if right_is_clear():
                    turn_right()
                    move()
                    if right_is_clear():
                        turn_around()
                        move()
                        turn_left()
                        build_wall()
                        turn_left()
                    else:
                        turn_around()
                        move()
                        turn_around()
                        search()
                else:
                    turn_right()
                    search()
    else:
        if front_is_clear():
            move()
        else:
            turn_left()

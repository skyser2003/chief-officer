﻿# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
# The game starts here.

init python: 
    import random
        
label start:
    call opening
    call first_class
    call second_class
    call third_class
    call forth_class
    call fifth_class
    call sixth_class
    call seventh_class
    call afterschool
    call ending
return

label activity:
    scene bg_class

    $ a = random.randint(0, 31)
    
    if a == 1:
        menu:
            "어디로 갈까?"
            "화장실":
                call place_toilet_men
                pass
            "체육관":
                call place_gym
                pass
            "수위실":
                call place_security_office
                pass
            "구교사":
                call place_old_school
                pass
            "운동장":
                call place_ground
                pass
            "교무실":
                call place_teachers_room
                pass
    if a == 2:
        menu:
            "어디로 갈까?"
            "체육관":
                call place_gym
                pass
            "화장실":
                call place_toilet
                pass
    if a == 3:
        menu:
            "어디로 갈까?"
            "수위실":
                call place_security_office
                pass
            "화장실":
                call place_toilet
                pass
    if a == 4:
        menu:
            "어디로 갈까?"
            "구교사":
                call place_old_school
                pass
            "화장실":
                call place_toilet
                pass
    if a == 5:
        menu:
            "어디로 갈까?"
            "운동장":
                call place_ground
                pass
            "화장실":
                call place_toilet
                pass
    if a == 6:
        menu:
            "어디로 갈까?"
            "교무실":
                call place_teachers_room
                pass
            "화장실":
                call place_toilet
                pass
    if a == 7:
        menu:
            "어디로 갈까?"
            "화장실":
                call place_toilet
                pass
            "체육관":
                call place_gym
                pass
    if a == 8:
        menu:
            "어디로 갈까?"
            "수위실":
                call place_security_office
                pass
            "체육관":
                call place_gym
                pass
    if a == 9:
        menu:
            "어디로 갈까?"
            "구교사":
                call place_old_school
                pass
            "체육관":
                call place_gym
                pass
    if a == 10:
        menu:
            "어디로 갈까?"
            "운동장":
                call place_ground
                pass
            "체육관":
                call place_gym
                pass
    if a == 11:
        menu:
            "어디로 갈까?"
            "교무실":
                call place_teachers_room
                pass
            "체육관":
                call place_gym
                pass
    if a == 12:
        menu:
            "어디로 갈까?"
            "화장실":
                call place_toilet
                pass
            "수위실":
                call place_security_office
                pass
    if a == 13:
        menu:
            "어디로 갈까?"
            "체육관":
                call place_gym
                pass
            "수위실":
                call place_security_office
                pass
    if a == 14:
        menu:
            "어디로 갈까?"
            "구교사":
                call place_old_school
                pass
            "수위실":
                call place_security_office
                pass
    if a == 15:
        menu:
            "어디로 갈까?"
            "운동장":
                call place_ground
                pass
            "수위실":
                call place_security_office
                pass
    if a == 16:
        menu:
            "어디로 갈까?"
            "교무실":
                call place_teachers_room
                pass
            "수위실":
                call place_security_office
                pass
    if a == 17:
        menu:
            "어디로 갈까?"
            "화장실":
                call place_toilet
                pass
            "구교사":
                call place_old_school
                pass
    if a == 18:
        menu:
            "어디로 갈까?"
            "체육관":
                call place_gym
                pass
            "구교사":
                call place_old_school
                pass
    if a == 19:
        menu:
            "어디로 갈까?"
            "수위실":
                call place_security_office
                pass
            "구교사":
                call place_old_school
                pass
    if a == 20:
        menu:
            "어디로 갈까?"
            "운동장":
                call place_ground
                pass
            "구교사":
                call place_old_school
                pass
    if a == 21:
        menu:
            "어디로 갈까?"
            "교무실":
                call place_teachers_room
                pass
            "구교사":
                call place_old_school
                pass
    if a == 22:
        menu:
            "어디로 갈까?"
            "화장실":
                call place_toilet
                pass
            "운동장":
                call place_ground
                pass
    if a == 23:
        menu:
            "어디로 갈까?"
            "체육관":
                call place_gym
                pass
            "운동장":
                call place_ground
                pass
    if a == 24:
        menu:
            "어디로 갈까?"
            "수위실":
                call place_security_office
                pass
            "운동장":
                call place_ground
                pass
    if a == 25:
        menu:
            "어디로 갈까?"
            "구교사":
                call place_old_school
                pass
            "운동장":
                call place_ground
                pass
    if a == 26:
        menu:
            "어디로 갈까?"
            "교무실":
                call place_teachers_room
                pass
            "운동장":
                call place_ground
                pass
    if a == 27:
        menu:
            "어디로 갈까?"
            "화장실":
                call place_toilet
                pass
            "교무실":
                call place_teachers_room
                pass
    if a == 28:
        menu:
            "어디로 갈까?"
            "체육관":
                call place_gym
                pass
            "교무실":
                call place_teachers_room
                pass
    if a == 29:
        menu:
            "어디로 갈까?"
            "수위실":
                call place_security_office
                pass
            "교무실":
                call place_teachers_room
                pass
    if a == 30:
        menu:
            "어디로 갈까?"
            "구교사":
                call place_old_school
                pass
            "교무실":
                call place_teachers_room
                pass
    if a == 31:
        menu:
            "어디로 갈까?"
            "운동장":
                call place_ground
                pass
            "교무실":
                call place_teachers_room
                pass


    return    

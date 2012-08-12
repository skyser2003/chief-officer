# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
# The game starts here.

init python: 
    import random
    
    heroine_love = dict(ghost = 00000)
    heroine_love.setdefault("boku", 0)
    heroine_love.setdefault("ghost", 0)
    heroine_love.setdefault("robot", 0)
    heroine_love.setdefault("sports_woman", 0)
    heroine_love.setdefault("trainee", 0)
    heroine_love.setdefault("yo", 0)
        
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
return

label activity:
    scene bg_class

    $ a = random.randint(1, 1)
    
    if a == 1:
        menu:
            "어디로 갈까?"
            "화장실":
                call place_toilet
                return
            "체육관":
                call place_gym
                return
            "수위실":
                call place_security_office
                return
            "구교사":
                call place_old_school
                return
            "운동장":
                call place_ground
                return
            "교무실":
                call place_teachers_room
                return
    if a == 2:
        menu:
            "어디로 갈까?"
            "체육관":
                call place_gym
                return
            "화장실":
                call place_toilet
                return
    if a == 3:
        menu:
            "어디로 갈까?"
            "수위실":
                call place_security_office
                return
            "화장실":
                call place_toilet
                return
    if a == 4:
        menu:
            "어디로 갈까?"
            "구교사":
                call place_old_school
                return
            "화장실":
                call place_toilet
                return
    if a == 5:
        menu:
            "어디로 갈까?"
            "운동장":
                call place_ground
                return
            "화장실":
                call place_toilet
                return
    if a == 6:
        menu:
            "어디로 갈까?"
            "교무실":
                call place_teachers_room
                return
            "화장실":
                call place_toilet
                return
    if a == 7:
        menu:
            "어디로 갈까?"
            "화장실":
                call place_toilet
                return
            "체육관":
                call place_gym
                return
    if a == 8:
        menu:
            "어디로 갈까?"
            "수위실":
                call place_security_office
                return
            "체육관":
                call place_gym
                return
    if a == 9:
        menu:
            "어디로 갈까?"
            "구교사":
                call place_old_school
                return
            "체육관":
                call place_gym
                return
    if a == 10:
        menu:
            "어디로 갈까?"
            "운동장":
                call place_ground
                return
            "체육관":
                call place_gym
                return
    if a == 11:
        menu:
            "어디로 갈까?"
            "교무실":
                call place_teachers_room
                return
            "체육관":
                call place_gym
                return
    if a == 12:
        menu:
            "어디로 갈까?"
            "화장실":
                call place_toilet
                return
            "수위실":
                call place_security_office
                return
    if a == 13:
        menu:
            "어디로 갈까?"
            "체육관":
                call place_gym
                return
            "수위실":
                call place_security_office
                return
    if a == 14:
        menu:
            "어디로 갈까?"
            "구교사":
                call place_old_school
                return
            "수위실":
                call place_security_office
                return
    if a == 15:
        menu:
            "어디로 갈까?"
            "운동장":
                call place_ground
                return
            "수위실":
                call place_security_office
                return
    if a == 16:
        menu:
            "어디로 갈까?"
            "교무실":
                call place_teachers_room
                return
            "수위실":
                call place_security_office
                return
    if a == 17:
        menu:
            "어디로 갈까?"
            "화장실":
                call place_toilet
                return
            "구교사":
                call place_old_school
                return
    if a == 18:
        menu:
            "어디로 갈까?"
            "체육관":
                call place_gym
                return
            "구교사":
                call place_old_school
                return
    if a == 19:
        menu:
            "어디로 갈까?"
            "수위실":
                call place_security_office
                return
            "구교사":
                call place_old_school
                return
    if a == 20:
        menu:
            "어디로 갈까?"
            "운동장":
                call place_ground
                return
            "구교사":
                call place_old_school
                return
    if a == 21:
        menu:
            "어디로 갈까?"
            "교무실":
                call place_teachers_room
                return
            "구교사":
                call place_old_school
                return
    if a == 22:
        menu:
            "어디로 갈까?"
            "화장실":
                call place_toilet
                return
            "운동장":
                call place_ground
                return
    if a == 23:
        menu:
            "어디로 갈까?"
            "체육관":
                call place_gym
                return
            "운동장":
                call place_ground
                return
    if a == 24:
        menu:
            "어디로 갈까?"
            "수위실":
                call place_security_office
                return
            "운동장":
                call place_ground
                return
    if a == 25:
        menu:
            "어디로 갈까?"
            "구교사":
                call place_old_school
                return
            "운동장":
                call place_ground
                return
    if a == 26:
        menu:
            "어디로 갈까?"
            "교무실":
                call place_teachers_room
                return
            "운동장":
                call place_ground
                return
    if a == 27:
        menu:
            "어디로 갈까?"
            "화장실":
                call place_toilet
                return
            "교무실":
                call place_teachers_room
                return
    if a == 28:
        menu:
            "어디로 갈까?"
            "체육관":
                call place_gym
                return
            "교무실":
                call place_teachers_room
                return
    if a == 29:
        menu:
            "어디로 갈까?"
            "수위실":
                call place_security_office
                return
            "교무실":
                call place_teachers_room
                return
    if a == 30:
        menu:
            "어디로 갈까?"
            "구교사":
                call place_old_school
                return
            "교무실":
                call place_teachers_room
                return
    if a == 31:
        menu:
            "어디로 갈까?"
            "운동장":
                call place_ground
                return
            "교무실":
                call place_teachers_room
                return

    return    

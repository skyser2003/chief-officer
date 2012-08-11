# You can place the script of your game in this file.

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
    
<<<<<<< HEAD
    $ a = random.randint(0, 11)
    
    if a == 1:
        menu:
            "어디로 갈까?"
            "남자 화장실":
                call place_toilet_men
                pass
            "여자 화장실":
                call place_toilet_women
                pass
            "체육관":
                call place_gym
                pass
            "음악실":
                call place_music_room
                pass
            "식당":
                call place_cafeteria
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
            "양호실":
                call place_infirmary
                pass
            "방송실":
                call place_broad
                pass
            "아무곳도 가지 않는다":
                call place_do_nothing
                pass
    if a == 2:
         menu:
            "어디로 갈까?"
            "남자 화장실":
                call place_toilet_men
                pass
            "방송실":
                call place_broad
                pass
            "아무곳도 가지 않는다":
                call place_do_nothing
                pass
    if a == 3:
        menu:
            "어디로 갈까?"
            "체육관":
                call place_gym
                pass
            "방송실":
                call place_broad
                pass
            "구교사":
                call place_old_school
                pass
    if a == 4:
        menu:
            "어디로 갈까?"
            "식당":
                call place_cafeteria
                pass
            "아무곳도 가지 않는다":
                call place_do_nothing
                pass
            "여자 화장실":
                call place_toilet_women
                pass
    if a == 5:
        menu:
            "어디로 갈까?"
            "음악실":
                call place_music_room
                pass
            "수위실":
                call place_security_office
                pass
            "운동장":
                call place_ground
                pass
            
    if a == 6:
        menu:
            "어디로 갈까?"
            "식당":
                call place_cafeteria
                pass
            "방송실":
                call place_broad
                pass
            "양호실":
                call place_infirmary
                pass
    if a == 7:
        menu:
            "어디로 갈까?"
            "구교사":
                call place_old_school
                pass
            "여자 화장실":
                call place_toilet_women
                pass
            "아무곳도 가지 않는다":
                call place_do_nothing
                pass
            "식당":
                call place_cafeteria
                pass
    if a == 8:
        menu:
            "어디로 갈까?"
            "양호실":
                call place_infirmary
                pass
            "구교사":
                call place_old_school
                pass
            "수위실":
                call place_security_office
                pass
            "방송실":
                call place_broad
                pass
    if a == 9:
        menu:
            "어디로 갈까?"
            "체육관":
                call place_gym
                pass
            "식당":
                call place_cafeteria
                pass
            "운동장":
                call place_ground
                pass
            "여자 화장실":
                call place_toilet_women
                pass
    if a == 10:
        menu:
            "어디로 갈까?"
            "방송실":
                call place_broad
                pass
            "구교사":
                call place_old_school
                pass
            "식당":
                call place_cafeteria
                pass
            "수위실":
                call place_security_office
                pass
    if a == 11:
        menu:
            "어디로 갈까?"
            "아무곳도 가지 않는다":
                call place_do_nothing
                pass
            "음악실":
                call place_music_room
                pass
            "수위실":
                call place_security_office
                pass
            "운동장":
                call place_ground
                pass
    return    
=======
    menu:
        "어디로 갈까?"
        "체육관":
            call place_gym
            pass
        "음악실":
            call place_music_room
            pass
        
    call after_school

return    
>>>>>>> 07061dd409

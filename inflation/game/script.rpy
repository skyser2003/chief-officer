# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
# The game starts here.

label start:
    call activity
return

label activity:
    scene bg_class
    
    menu:
        "어디로 갈까?"
        "체육관":
            call place_gym
            pass
        "음악식":
            call place_music_room
            pass
        
    return    

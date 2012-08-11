# You can place the script of your game in this file.

init python:
    import random
    
    class Heroine:
        def __init__(self,name,dir):
            self.name = name
            self.feeling = 0
            self.imgDir = dir
            
        def toString(self):
            return str(self.feeling)
            
# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image health_room = im.Scale("img/bg/health_room.jpg",config.screen_width,config.screen_height)
image music_room = im.Scale("img/bg/music_room.jpg",config.screen_width,config.screen_height)

define hMadoka = Heroine("마도카","img/heroine/madoka.png")
define heroines = [hMadoka,]

image iMadoka = hMadoka.imgDir

# Declare characters used by this game.
define e = Character('마도카', color="#c8ffc8")
define chars = [e,]

# The game starts here.
label start:

    e "You've created a new Ren'Py game."
    e "Once you add a story, pictures, and music, you can release it to the world!"

    call madoka
return

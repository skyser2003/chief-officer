init python:
    import random

label madoka:
#    scene health_room with dissolve    
    $ heroineNo = 0
    
    show image "img/heroine/Madoka.png"
    e"안녕"

    menu:
        "꺼져":
            "너도"
            $ heroines[heroineNo].feeling = heroines[heroineNo].feeling + 1000
            pass
        "엿먹어":
            "너나"
            $ heroines[heroineNo].feeling = heroines[heroineNo].feeling + 100000
            pass
        "배고파":
            "나도"
            $ heroines[heroineNo].feeling = heroines[heroineNo].feeling + 10000033
            pass
    $ tx = heroines[heroineNo].feeling
    $e(heroines[heroineNo].toString())
    
    return

label ending:
    scene bg_ending with dissolve
    define heroine_love = dict(ghost = 100000)
    
    python:
        matching_heroine_love = []
        for name in heroine_love:
            if(heroine_love[name] >= love_standard):
                matching_heroine_love.append(name)
    
    if(len(matching_heroine_love) == 0):
        #Bad ending 1.  No heroine in love
        "Bad ending 1"
    elif(len(matching_heroine_love) > 1):
        #Bad ending 2.  More than one heroine in love
        "Bad ending 2"
    else:
        #Happy ending.  One heroine in love!
        "Happy ending"

    return

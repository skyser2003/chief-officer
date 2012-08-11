label ending:
    scene bg_ending with dissolve
    define heroines = dict(ghost = 100000)
    
    python:
        matching_heroines = []
        for name in heroines:
            if(heroines[name] >= love_standard):
                matching_heroines.append(name)
    
    if(len(matching_heroines) == 0):
        #Bad ending 1.  No heroine in love
        "Bad ending 1"
    elif(len(matching_heroines) > 1):
        #Bad ending 2.  More than one heroine in love
        "Bad ending 2"
    else:
        #Happy ending.  One heroine in love!
        "Happy ending"

    return

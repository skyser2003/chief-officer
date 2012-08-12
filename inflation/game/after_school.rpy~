label afterschool:
    scene bg_afterschool with dissolve
    "하교"
    
    python:
        matching_heroine_love = []
        for name in heroine_love:
            if(heroine_love[name] >= love_standard):
                matching_heroine_love.append(name)
    
    if len(matching_heroine_love) == 1:
        #Happy ending.  One heroine in love!
        call happy_ending
    else:
        # Bad Ending.
        call bad_ending
    
    return

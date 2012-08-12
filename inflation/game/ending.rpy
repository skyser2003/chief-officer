label bad_ending:
    $ cnt = 4
    show boku_3 at Position(xpos = 1.0 / cnt)
    show ghost_3 at Position(xpos = 2.0 / cnt)
    show yo_3 at Position(xpos = 3.0 / cnt)
    "Bad ending"
    return
    
label happy_ending:
    $ heroine_name = matching_heroine_love[0]
    
    if name == 'boku':
        show boku_2
    elif name == 'ghost':
        show ghost_2
    elif name == 'robot':
        show robot_2
    elif name == 'sports_woman':
        show sports_woman_2
    elif name == 'trainee':
        show trainee_2
    elif name == 'yo':
        show yo_2
    
    return
    

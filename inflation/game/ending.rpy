label bad_ending:

    python:
        bad_heroines = []
        for name in heroine_love:
            if(heroine_love[name] != 0):
                bad_heroines.append(name)
        
        number = len(bad_heroines)
        j  = 0
        if(number != 0):
            for i in bad_heroines:
                j += 1
                renpy.show(i + "_3",at_list = [Position(xpos = 1.0 * j / (number + 1))])
        else:
            for name in heroine_love:
                j += 1
                renpy.show(name + "_3",at_list = [Position(xpos = 1.0 * j / (number + 1))])

    "Bad ending"
    return
    
label happy_ending:
    $ heroine_name = matching_heroine_love[0]
    $ renpy.show(heroine_name + "_2")
    
    "기다리고 있었어!  %(hero_name)s!  집에 같이 가자"
    
    menu:
        "그래":
            "Happy Ending"
        "싫어":
            $ renpy.call_in_new_context(heroine_name + "_hide")
            $ renpy.show(heroine_name + "_1")
            "너무해...  내가 싫은 거구나!"
            $ renpy.call_in_new_context(heroine_name + "_hide")
            $ renpy.show(heroine_name + "_3")
            "이렇게 된 이상...  에잇!"
            
            "Game Over"
    return
    

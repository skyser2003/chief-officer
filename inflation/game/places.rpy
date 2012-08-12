label place_toilet:
    scene bg_toilet
    "화장실 앞이다."
    
    $ list = ['yo']
    $ rand = random.randint(0,len(list)-1)
    $ renpy.call_in_new_context(list[rand] + "_toilet")

    return

label place_gym:
    scene bg_gym
    "체육관이다."
    
    $ list = ['boku','sports_woman']
    $ rand = random.randint(0,len(list)-1)
    $ renpy.call_in_new_context(list[rand] + "_gym")
    
    return

label place_security_office:
    scene bg_security_office
    "수위실이다."
    
    $ list = ['ghost','robot','trainee']
    $ rand = random.randint(0,len(list)-1)
    $ renpy.call_in_new_context(list[rand] + "_security_office")
    
    return

label place_old_school:
    scene bg_old_school
    "구교사다."

    $ list = ['ghost','robot', 'trainee']
    $ rand = random.randint(0,len(list)-1)
    $ renpy.call_in_new_context(list[rand] + "_old_school")
    
    return

label place_ground:
    scene bg_ground
    "운동장이다."
    
    $ list = ['boku','sports_woman']
    $ rand = random.randint(0,len(list)-1)
    $ renpy.call_in_new_context(list[rand] + "_ground")
    
    return
    
label place_teachers_room:
    scene bg_teachers_room
    "교무실이다."
    
    $ list = ['robot','trainee']
    $ rand = random.randint(0,len(list)-1)
    $ renpy.call_in_new_context(list[rand] + "_teachers_room")
    
    return


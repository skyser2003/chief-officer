label place_toilet_men:
    scene bg_toilet_men
    "남자 화장실 앞이다."
    
    $ list = ['boku', 'sports_woman', 'trainee', 'yo']
    $ rand = random.randint(0,len(list)-1)
    $ renpy.call_in_new_context(list[rand] + "_toilet_men")

    return

label place_toilet_women:
    scene bg_toilet_women
    "여자 화장실 앞이다."
    
    $ list = ['boku', 'sports_woman', 'trainee', 'yo']
    $ rand = random.randint(0,len(list)-1)
    $ renpy.call_in_new_context(list[rand] + "_toilet_women")

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
    
    $ list = ['ghost','robot']
    $ rand = random.randint(0,len(list)-1)
    $ renpy.call_in_new_context(list[rand] + "_security_office")
    
    return

label place_old_school:
    scene bg_old_school
    "구교사다."

    $ list = ['ghost','robot']
    $ rand = random.randint(0,len(list)-1)
    $ renpy.call_in_new_context(list[rand] + "_old_school")
    
    return

label place_ground:
    scene bg_ground
    "운동장이다."
    
    $ list = ['boku','sports_woman','yo']
    $ rand = random.randint(0,len(list)-1)
    $ renpy.call_in_new_context(list[rand] + "_ground")
    
    return

label place_do_nothing:
    scene bg_class
    "아무것도 안 할랭"
    return


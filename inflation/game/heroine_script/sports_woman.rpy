define sports_woman = Character("운동하는 여자",color="#000000")

label sports_woman_global_1:
    "운동하는 여자 - 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label sports_woman_global_2:
    "운동하는 여자 - 공통 2"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label sports_woman_global_3:
    "운동하는 여자 - 공통 3"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
 
label sports_woman_gym_limit_1:
    "운동하는 여자 - 체육관 한정 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
              
label sports_woman_ground_1:
    "운동하는 여자 - 운동장 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label sports_woman_ground_2:
    "운동하는 여자 - 운동장 공통 2"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label sports_woman_ground_3:
    "운동하는 여자 - 운동장 공통 3"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
     
label sports_woman_gym:
    $ a = random.randint(0, 3)
    
    if a == 0:
        call sports_woman_global_1
    if a == 1:
        call sports_woman_global_2
    if a == 2:
        call sports_woman_global_3
    if a == 4:
        call sports_woman_gym_limit_1
     
    return
     
label sports_woman_ground:
    $ a = random.randint(0, 5)
    
    if a == 0:
        call sports_woman_global_1
    if a == 1:
        call sports_woman_global_2
    if a == 2:
        call sports_woman_global_3
    if a == 3:
        call sports_woman_ground_1
    if a == 4:
        call sports_woman_ground_2
    if a == 5:
        call sports_woman_ground_3
     
    return
   

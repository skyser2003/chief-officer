label pianist_global_1:
    "피아니스트 - 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label pianist_global_2:
    "피아니스트 - 공통 2"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label pianist_global_3:
    "피아니스트 - 공통 3"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return

label pianist_toilet_men_1:
    "피아니스트 - 남장실 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
 
label pianist_toilet_women_1:
    "피아니스트 - 여장실 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
  
label pianist_toilet_women_2:
    "피아니스트 - 여장실 공통 2"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
   
label pianist_music_room_1:
    "피아니스트 - 음악실 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label pianist_music_room_limit_1:
    "피아니스트 - 음악실 한정 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
     
label pianist_cafeteria_1:
    "피아니스트 - 식당 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
 
label pianist_toilet_men:
    $ a = random.randint(0, 3)
    
    if a == 0:
        call pianist_global_1
    if a == 1:
        call pianist_global_2
    if a == 2:
        call pianist_global_3
    if a == 3:
        call pianist_toilet_men_1
        
    return
    
label pianist_toilet_women:
    $ a = random.randint(0, 4)
    
    if a == 0:
        call pianist_global_1
    if a == 1:
        call pianist_global_2
    if a == 2:
        call pianist_global_3
    if a == 3:
        call pianist_toilet_women_1
    if a == 4:
        call pianist_toilet_women_2
        
    return
    
label pianist_toilet_music_room:
    $ a = random.randint(0, 4)
    
    if a == 0:
        call pianist_global_1
    if a == 1:
        call pianist_global_2
    if a == 2:
        call pianist_global_3
    if a == 3:
        call pianist_music_room_1
    if a == 4:
        call pianist_music_room_limit_1
        
    return
 
label pianist_cafeteria:
    $ a = random.randint(0, 3)
    
    if a == 0:
        call pianist_global_1
    if a == 1:
        call pianist_global_2
    if a == 2:
        call pianist_global_3
    if a == 3:
        call pianist_cafeteria_1
        
    return
  

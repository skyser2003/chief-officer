label announcer_global_1:
    "방송 - 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label announcer_global_2:
    "방송 - 공통 2"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label announcer_global_3:
    "방송 - 공통 3"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label 
    
label announcer_broad_limit_1:
    "방송 - 방송실 한정 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label 
    
label announcer_toilet_men_1:
    "방송 - 남장실 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label 
    
label announcer_toilet_women_1:
    "방송 - 여장실 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label 
        
label announcer_toilet_women_2:
    "방송 - 여장실 공통 2"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label 
   
label announcer_music_room_1:
    "방송 - 음악실 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label 

label announcer_broad:
    $ a = random.randint(0, 3)
    
    if a == 0:
        call announcer_global_1
    if a == 1:
        call announcer_global_2
    if a == 2:
        call announcer_global_3
    if a == 3:
        call announcer_broad_limit_1
        
    return
    
label announcer_toilet_men:
    $ a = random.randint(0, 3)
    
    if a == 0:
        call announcer_global_1
    if a == 1:
        call announcer_global_2
    if a == 2:
        call announcer_global_3
    if a == 3:
        call announcer_toilet_men_1
        
    return
    
label announcer_toilet_women:
    $ a = random.randint(0, 4)
    
    if a == 0:
        call announcer_global_1
    if a == 1:
        call announcer_global_2
    if a == 2:
        call announcer_global_3
    if a == 3:
        call announcer_toilet_women_1
    if a == 4:
        call announcer_toilet_women_2
        
    return
      
label announcer_music_room:
    $ a = random.randint(0, 3)
    
    if a == 0:
        call announcer_global_1
    if a == 1:
        call announcer_global_2
    if a == 2:
        call announcer_global_3
    if a == 3:
        call announcer_music_room_1
     
    return
  

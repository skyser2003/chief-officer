label boku_global_1:
    "보쿠소녀 - 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label boku_global_2:
    "보쿠소녀 - 공통 2"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label boku_global_3:
    "보쿠소녀 - 공통 3"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return

label boku_toilet_men_1:
    "보쿠소녀 - 남장실 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label boku_toilet_women_1:
    "보쿠소녀 - 여장실 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
     
label boku_toilet_women_2:
    "보쿠소녀 - 여장실 공통 2"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
       
label boku_gym_1:
    "방송 - 체육관 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
       
label boku_cafeteria_1:
    "방송 - 식당 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
       
label boku_cafeteria_2:
    "방송 - 식당 공통 2"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
     
label boku_ground_1:
    "보쿠소녀 - 운동장 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label boku_ground_2:
    "보쿠소녀 - 운동장 공통 2"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
   
label boku_ground_limit_1:
    "보쿠소녀 - 운동장 한정 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
       
label boku_infirmary_1:
    "방송 - 양호실 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
  
label boku_toilet_men:
    $ a = random.randint(0, 3)
    
    if a == 0:
        call boku_global_1
    if a == 1:
        call boku_global_2
    if a == 2:
        call boku_global_3
    if a == 3:
        call boku_toilet_men_1
        
    return
    
label boku_toilet_women:
    $ a = random.randint(0, 3)
    
    if a == 0:
        call boku_global_1
    if a == 1:
        call boku_global_2
    if a == 2:
        call boku_global_3
    if a == 3:
        call boku_toilet_women_1
        
    return
      
label boku_gym:
    $ a = random.randint(0, 3)
    
    if a == 0:
        call boku_global_1
    if a == 1:
        call boku_global_2
    if a == 2:
        call boku_global_3
    if a == 3:
        call boku_gym_1
     
    return
     
label boku_cafeteria:
    $ a = random.randint(0, 4)
    
    if a == 0:
        call boku_global_1
    if a == 1:
        call boku_global_2
    if a == 2:
        call boku_global_3
    if a == 3:
        call boku_cafeteria_1
    if a == 4:
        call boku_cafeteria_2
        
    return
         
label boku_ground:
    $ a = random.randint(0, 5)
    
    if a == 0:
        call boku_global_1
    if a == 1:
        call boku_global_2
    if a == 2:
        call boku_global_3
    if a == 3:
        call boku_ground_limit_1
    if a == 4:
        call boku_ground_1
    if a == 5:
        call boku_ground_2
     
    return
   

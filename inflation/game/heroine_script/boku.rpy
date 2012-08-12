define robot = Character("보쿠소녀",color="#000000")

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

label boku_ground_1:
    "보쿠소녀 - 화장실 한정 1"
    
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
       
label boku_ground_3:
    "보쿠소녀 - 운동장 공통 3"
   
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

label boku_show:
    $ love = heroine_love['boku']
    
    if love < 50000:
        show boku_1
    elif love < 100000:
        show boku_2
    else:
        show boku_3
        
    return

label boku_hide:
    hide boku_1
    hide boku_2
    hide boku_3
    return

label boku_gym:
    $ a = random.randint(0, 2)
    
    call boku_show
    
    if a == 0:
        call boku_global_1
    if a == 1:
        call boku_global_2
    if a == 2:
        call boku_global_3
      
    call boku_hide    
        
    return
          
label boku_ground:
    $ a = random.randint(0, 6)
    
    call boku_show
    
    if a == 0:
        call boku_global_1
    if a == 1:
        call boku_global_2
    if a == 2:
        call boku_global_3
    if a == 3:
        call boku_ground_1
    if a == 4:
        call boku_ground_2
    if a == 5:
        call boku_ground_3
    if a == 6:
        call boku_ground_limit_1
    
    call boku_hide    
        
    return
   

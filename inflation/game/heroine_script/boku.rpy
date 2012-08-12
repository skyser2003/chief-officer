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

label boku_toilet_1:
    "보쿠소녀 - 화장실 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return

label boku_toilet_limit_1:
    "방송 - 화장실 한정 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
       
label boku_toilet:
    $ a = random.randint(0, 4)
    
    if a == 0:
        call boku_global_1
    if a == 1:
        call boku_global_2
    if a == 2:
        call boku_global_3
    if a == 3:
        call boku_toilet_1
    if a == 4:
        call boku_toilet_limit_1
        
    return
   

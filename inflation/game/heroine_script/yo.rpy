define yo = Character("요자",color="#000000")

label yo_global_1:
    "요자- 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label yo_global_2:          
    "요자 - 공통 2"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label yo_global_3:
    "요자 - 공통 3"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return

label yo_toilet_1:
    "귀신 - 화장실 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return

label yo_toilet_limit_1:
    "요자 - 화장실 한정 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return

label yo_toilet_limit_2:
    "귀신 - 화장실 한정 2"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return

label yo_toilet:
    $ a = random.randint(0, 5)
    
    if a == 0:
        call yo_global_1
    if a == 1:
        call yo_global_2
    if a == 2:
        call yo_global_3
    if a == 3:
        call yo_toilet_1
    if a == 4:
        call yo_toilet_limit_1
    if a == 5:
        call yo_toilet_limit_2
        
    return


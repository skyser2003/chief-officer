define ghost = Character("유령",color="#000000")

label ghost_global_1:
    "귀신 - 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label ghost_global_2:
    "귀신 - 공통 2"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label ghost_global_3:
    "귀신 - 공통 3"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return

label ghost_old_school_1:
    "귀신 - 구교사 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return

label ghost_security_office:
    $ a = random.randint(0, 2)
    
    if a == 0:
        call ghost_global_1
    if a == 1:
        call ghost_global_2
    if a == 2:
        call ghost_global_3
        
    return
    
label ghost_old_school:
    $ a = random.randint(0, 3)
    
    if a == 0:
        call ghost_global_1
    if a == 1:
        call ghost_global_2
    if a == 2:
        call ghost_global_3
    if a == 3:
        call ghost_old_school_1
        
    return


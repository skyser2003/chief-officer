define robot = Character("로봇",color="#000000")

label robot_global_1:
    "로봇 - 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label robot_global_2:
    "로봇 - 공통 2"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label robot_global_3:
    "로봇 - 공통 3"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return

label robot_security_office_limit_1:
    "로봇 - 수위실 한정 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return

label robot_old_school_1:
    "로봇 - 구교사 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label robot_show:
    $ love = heroine_love['robot']
    
    if love < 50000:
        show robot_1
    elif love < 100000:
        show robot_2
    else:
        show robot_3
        
    return

label robot_hide:
    hide robot_1
    hide robot_2
    hide robot_3
    return

  
label robot_security_office:
    $ a = random.randint(0, 3)
    
    call robot_show
    
    if a == 0:
        call robot_global_1
    if a == 1:
        call robot_global_2
    if a == 2:
        call robot_global_3
    if a == 3:
        call robot_security_office_limit_1
        
    call robot_hide    
        
    return
   
label robot_old_school:
    $ a = random.randint(0, 3)
    
    call robot_show
    
    if a == 0:
        call robot_global_1
    if a == 1:
        call robot_global_2
    if a == 2:
        call robot_global_3
    if a == 3:
        call robot_old_school_1
    
    call robot_hide
        
    return
    
label robot_teachers_room:
    $ a = random.randint(0, 2)
    
    call robot_show
    
    if a == 0:
        call robot_global_1
    if a == 1:
        call robot_global_2
    if a == 2:
        call robot_global_3
    
    call robot_hide
    
    return
 

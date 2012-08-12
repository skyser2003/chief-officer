define trainee = Character("교생",color="#000000")

label trainee_global_1:
    "교생 - 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label trainee_global_2:
    "교생 - 공통 2"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label trainee_global_3:
    "교생 - 공통 3"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return

label trainee_teachers_room_limit_1:
    "교생 - 교무실 한정 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return

label trainee_old_school_1:
    "교생 - 구교사 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
  
label trainee_security_office_1:
    "교생 - 수위실 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
       
label trainee_teachers_room:
    $ a = random.randint(0, 4)
    
    if a == 0:
        call trainee_global_1
    if a == 1:
        call trainee_global_2
    if a == 2:
        call trainee_global_3
    if a == 3:
        call trainee_toilet_1
    if a == 4:
        call trainee_teachers_room_limit_1
        
    return
         
label trainee_old_school:
    $ a = random.randint(0, 4)
    
    if a == 0:
        call trainee_global_1
    if a == 1:
        call trainee_global_2
    if a == 2:
        call trainee_global_3
    if a == 3:
        call trainee_toilet_1
    if a == 4:
        call trainee_old_school_1
        
    return
        
label trainee_teachers_roomt:
    $ a = random.randint(0, 4)
    
    if a == 0:
        call trainee_global_1
    if a == 1:
        call trainee_global_2
    if a == 2:
        call trainee_global_3
    if a == 3:
        call trainee_toilet_1
    if a == 4:
        call trainee_security_office_1
        
    return
  

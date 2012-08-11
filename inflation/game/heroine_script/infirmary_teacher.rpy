label infirmary_teacher_global_1:
    "양호선생 - 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label infirmary_teacher_global_2:
    "양호선생 - 공통 2"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label infirmary_teacher_global_3:
    "양호선생 - 공통 3"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return

label infirmary_teacher_toilet_men_1:
    "양호선생 - 남장실 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
 
label infirmary_teacher_toilet_women_1:
    "양호선생 - 여장실 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
 
label infirmary_teacher_toilet_women_2:
    "양호선생 - 여장실 공통 2"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return

label infirmary_teacher_infirmary_limit_1:
    "양호선생 - 양호실 한정 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return

label infirmary_teacher_infirmary_1:
    "양호선생 - 양호실 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return

label infirmary_teacher_toilet_men:
    $ a = random.randint(0, 3)
    
    if a == 0:
        call infirmary_teacher_global_1
    if a == 1:
        call infirmary_teacher_global_2
    if a == 2:
        call infirmary_teacher_global_3
    if a == 3:
        call infirmary_teacher_toilet_men_1
        
    return
    
label infirmary_teacher_toilet_women:
    $ a = random.randint(0, 4)
    
    if a == 0:
        call infirmary_teacher_global_1
    if a == 1:
        call infirmary_teacher_global_2
    if a == 2:
        call infirmary_teacher_global_3
    if a == 3:
        call infirmary_teacher_toilet_women_1
    if a == 4:
        call infirmary_teacher_toilet_women_2
        
    return

label infirmary_teacher_infirmary:
    $ a = random.randint(0, 4)
    
    if a == 0:
        call infirmary_teacher_global_1
    if a == 1:
        call infirmary_teacher_global_2
    if a == 2:
        call infirmary_teacher_global_3
    if a == 3:
        call infirmary_teacher_infirmary_1
    if a == 4:
        call infirmary_teacher_infirmary_limit_1
        
    return
   

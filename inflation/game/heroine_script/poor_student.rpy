define poor_student = Character("가난한 학생",color="#000000")

label poor_student_global_1:
    "가난한 학생 - 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label poor_student_global_2:
    "가난한 학생 - 공통 2"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label poor_student_global_3:
    "가난한 학생 - 공통 3"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return

label poor_student_toilet_men_1:
    "가난한 학생 - 남장실 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
 
label poor_student_toilet_women_1:
    "가난한 학생 -  여장실 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
 
label poor_student_toilet_women_2:
    "가난한 학생 -  여장실 공통 2"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
  
label poor_student_cafeteria_1:
    "가난한 학생 -  식당 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
  
label poor_student_cafeteria_2:
    "가난한 학생 -  식당 공통 2"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
  
label poor_student_cafeteria_limit_1:
    "가난한 학생 -  식당 한정 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
 
label poor_student_toilet_men:
    $ a = random.randint(0, 2)
    
    if a == 0:
        call poor_student_global_1
    if a == 1:
        call poor_student_global_2
    if a == 2:
        call poor_student_global_3
    if a == 3:
        call poor_student_toilet_men_1
        
    return
    
label poor_student_toilet_women:
    $ a = random.randint(0, 4)
    
    if a == 0:
        call poor_student_global_1
    if a == 1:
        call poor_student_global_2
    if a == 2:
        call poor_student_global_3
    if a == 3:
        call poor_student_toilet_women_1
    if a == 4:
        call poor_student_toilet_women_2
        
    return
 
label poor_student_cafeteria:
    $ a = random.randint(0, 5)
    
    if a == 0:
        call poor_student_global_1
    if a == 1:
        call poor_student_global_2
    if a == 2:
        call poor_student_global_3
    if a == 3:
        call poor_student_cafeteria_1
    if a == 4:
        call poor_student_cafeteria_1
    if a == 5:
        call poor_student_cafeteria_limit_1
        
    return
    

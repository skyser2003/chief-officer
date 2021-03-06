define sports_woman = Character("운동하는 여자",color="#FFFFFF")

label sports_woman_global_1:
    "앗 안녕?"
    A "(운동소녀가 나를 부른 거 같다)"
    menu:
        "대답한다":
            A "응 안녕 운동소녀야!"
            "운동소녀와 대화를 나누다 교실로 돌아갔다"
            $ heroine_love['sports_woman'] += 10000
            pass
        "무시한다":
            A "(귀찮으니까 그냥 가자...)"
            call sports_woman_hide
            show sports_woman_2
            sports_woman "헤헤 나를 무시하는 저 시크한 모습... 멋져!"
            $ heroine_love['sports_woman'] += 20000
            pass
        "시비를 건다":
            A "야 너 심심하면 나 부른다?  응?"
            sports_woman "미... 미안.  너무 반가워서..."
            call sports_woman_hide
            show sports_woman_2
            sports_woman "(헤헤 멋지다!)"
            "겁에 질려있는 듯한 운동소녀를 뒤로 하고 교실로 돌아왔다"
            $ heroine_love['sports_woman'] += 30000
            pass
        
    return
    
label sports_woman_global_2:
    A "으엉... 저기 운동하는 애는....  운동 소녀네?"
    
    menu:
        "말을 건다":
            A "운동소녀야!"
            sports_woman "어 안녕!"
            "운동소녀와 대화를 나누다가 교실로 돌아갔다"
            $ heroine_love['sports_woman'] += 10000
            pass
        "무시한다":
            A "(괜히 말 걸면 귀찮으니까 그냥 가야지)"
            pass
        "삥을 뜯는다":
            A "운동소녀!  돈 좀 있어?"
            sports_woman "어.. 있어.  줄께!"
            A "필요없어!"
            call sports_woman_hide
            show sports_woman_2
            sports_woman "(어머... 멋져!)"
            "돈을 가지고 교실로 돌아왔다"
            
            $ heroine_love['sports_woman'] += 30000
            pass
        
    return
    
label sports_woman_global_3:
    call sports_woman_hide
    A "으으 지금 나가면 운동소녀가 있을 거 같지만... 졸려.  안 나가야지..."
        
    return
 
label sports_woman_gym_limit_1:
    "짐을 옮기고 있는 운동여자가 보인다"
    sports_woman "이거 무거워서 그러는데 도와줄래?"
    menu:
        "역시 이런 건 도와줘야겠지?":
            sports_woman "고마워!"
            "운동여자를 도와준 뒤 교실로 돌아왔다"
            $ heroine_love['sports_woman'] += 10000
            pass
        "나도 내 발이 무거워서 도와줄 수 없어":
            sports_woman "뭔 소린지 모르겠지만 멋있어!"
            A "아 시간 다 됐다 교실로 돌아가야지."
            "낑낑되는 운동여자를 뒤로 하고 교실로 돌아왔다"
            $ heroine_love['sports_woman'] += 20000
            pass
        
    return
              
label sports_woman_ground_1:
    "운동하는 여자 - 운동장 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label sports_woman_ground_2:
    "운동하는 여자 - 운동장 공통 2"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label sports_woman_ground_3:
    "운동하는 여자 - 운동장 공통 3"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return

label sports_woman_show:
    $ love = heroine_love['sports_woman']
    
    if love < 50000:
        show sports_woman_1
    elif love < 100000:
        show sports_woman_2
    else:
        show sports_woman_3
        
    return

label sports_woman_hide:
    hide sports_woman_1
    hide sports_woman_2
    hide sports_woman_3
    return
    
label sports_woman_gym:
    show sports_woman_1
    
    $ a = random.randint(0, 3)
    
    call sports_woman_show
    
    if a == 0:
        call sports_woman_global_1
    if a == 1:
        call sports_woman_global_2
    if a == 2:
        call sports_woman_global_3
    if a == 4:
        call sports_woman_gym_limit_1
        
    call sports_woman_hide

    return
     
label sports_woman_ground:
    show sports_woman_1
    
    $ a = random.randint(0, 5)
    
    call sports_woman_show
    
    if a == 0:
        call sports_woman_global_1
    if a == 1:
        call sports_woman_global_2
    if a == 2:
        call sports_woman_global_3
    if a == 3:
        call sports_woman_ground_1
    if a == 4:
        call sports_woman_ground_2
    if a == 5:
        call sports_woman_ground_3
    
    call sports_woman_hide
                                       
    return


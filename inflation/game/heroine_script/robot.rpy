define robot = Character("로봇",color="#FFFFFF")

label robot_global_1:
    robot "삐비빅"
    
    menu:
        "로봇이 나를 부른 거 같다":
            A "응?  아 로봇이구나"
            "로봇과 대화를 나누다 교실로 돌아갔다"
            $ heroine_love['robot'] += 10000
            pass
        "무시한다":
            A "(귀찮으니 그냥 가자....)"
            call robot_hide
            show robot_2
            robot "......♥"
            "로봇을 무시한 채 교실로 돌아왔다"
            $ heroine_love['robot'] += 30000
            pass
        "시비를 건다":
            A "길가다 아무나 막 부르지!"
            robot "죄송합니다.  시정하겠습니다"
            call robot_hide
            show robot_1
            robot "♥"
            "겁에 질려있는 것 같은 로봇을 뒤로 하고 교실로 돌아왔다"
            $ heroine_love['robot'] += 30000
            pass
        
    return
    
label robot_global_2:
    A "어 지나가는 로봇이다"
    
    menu:
        "말을 건다":
            A "로봇아!"
            robot "안녕하세요.  오늘도 안녕하십니까"
            "로봇과 대화를 나누다 교실로 들어갔다"
            $ heroine_love['robot'] += 10000
            pass
        "무시한다":
            A "(괜히 말 걸면 귀찮으니까 가자)"
            pass
        "삥을 뜯는다":
            A "로봇아!  너 돈 좀 있냐?"
            robot "있습니다.  드리겠습니다"
            A "필요없어!"
            call robot_hide
            show robot_2
            robot "(멋있습니다)"
            "돈을 가지고 교실로 돌아왔다"
            $ heroine_love['robot'] += 30000
            pass
    return
    
label robot_global_3:
    call robot_hide
    "으엉 지금 나가면 로봇을 만날 거 같지만...  귀찮다 그냥 자야지"
    
    return

label robot_security_office_limit_1:
    "수위실에 들렀는데 로봇이 방전 위기!  충전을 도와주자"
    robot "장비를 정지합니다.... 정지하겠습니다...."
    menu:
        "왠지 저 태엽을 돌리면 될 거 같다":
            call robot_hide
            show robot_2
            robot "하아.....  하아.....  뚝."
            call robot_hide
            show robot_1
            robot "시스템 가동.  준비 완료.  감사합니다"
            A "응 그래"
            "가동된 로봇을 뒤로 하고 교실로 간다"
            pass
        "저 전개면 어차피 정지가 안 되잖아":
            robot "....."
            "다시 움직이기 시작한 로봇을 뒤로 하고 교실로 돌아왔다"
            pass
        
    return
    
label robot_old_school_1:
    call robot_hide
    A "(으엉 여긴 어디 난 누구...?)"
    A "(으으 갑자기 오싹한 느낌이 든다)"
    
    menu:
        "뒤를 돌아본다":
            show robot_1
            "왠 로봇이 서 있다"
            A "으악!  튀자"
            "열심히 교실로 도망쳤다"
            call robot_hide
            show robot_2
            robot "...."
            $ heroine_love['robot'] += 10000
            pass
        "그냥 나간다":
            A "으으... 아무래도 무서워.  그냥 나가야지"
            "교실로 돌아갔다"
            pass
        "소리를 질러 본다":
            show robot_1
            robot "......"
            A "깜짝이야!"
            robot "침입자 발견.  제거 준비"
            A "안 돼!"
            "열심히 교실로 도망쳤다"
            call robot_hide
            show robot_2
            robot "...."
            $ heroine_love['robot'] += 30000
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
    show robot_1
    
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
    show robot_1
    
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
    show robot_1
    
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


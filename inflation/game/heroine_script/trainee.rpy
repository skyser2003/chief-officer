define trainee = Character("교생",color="#000000")

label trainee_global_1: #FIXME
    trainee  "%(hero_name)s야!"
    menu:
        "(B가 나를 부른 것 같다.)"
        "대답한다.":
            A   "응? 아 B구나"
            "B와 대화를 나누다 교실로 돌아갔다" 
            return
        "무시한다.":
            A  "(귀찮으니 그냥 가자)...."
            trainee   "와! 저 나를 무시하는 시크한 모습!.....멋져!"
            "B를 무시한체 교실로 돌아왔다"
            return
        "시비를 건다.":
            A "길가다 아무나 막 부르고 똥오줌 못가리지!"
            trainee "미....미안.... 반..가워서..."
            trainee "(저 강한 모습... 정말 멋져!)"
            trainee "겁에 질려있는것같은 B를 뒤로한채 교실로 돌아왔다"
        
    return
    
label trainee_global_2: #FIXME
    menu:
        A "(어 B가 지나간다.)"
        "말을 건다.":
            A "B야!"
            trainee "어? %(hero_name)s구나!"
            "B와 대화를 나누다 교실로 돌아갔다."
            return
        "무시한다.":
            A "(괜히 말걸면 귀찮으니깐 그냥 가자)"
            return
        "삥을 뜯는다.":
            A "야 B! 돈좀 있냐?"
            trainee "드...드리겠습니다!"
            A "필요없어!"
            trainee "(어머 저 박력! 멋져!)"
            "돈을 가지고 교실로 돌아왔다"
        
    return
    
label trainee_global_3: #FIXME
    call trainee_hide
    A "아 귀찮다 그냥 자야지..,"
    "(그렇게 그는 생각하는 것을 그만두었다.)"
        
    return

label trainee_teachers_room_limit_1: #FIXME
    A "응? 저사람은 B?"
    menu:
        trainee "아 A! 잘됐다 마침. 심부름좀 해줄래?"
        "선생님의 부탁이니..":
            A "네 그럴게요"
            trainee "고마워 %(hero_name)s!"
            "(%(hero_name)s는 정말 착한아이구나!)"
            "(심부름을 한뒤 교실로 돌아왔다.)"
        "이럴때 필요한건 뭐?":
            "나는 한줄기 바람이되어 교실로 뛰었다."
            trainee "얘! 실내에서 뛰면 안돼!"
            "(저 빠른 결단력! 멋져!)"
            "심부름을 무시한체 빠르게 교실로 돌아왔다."
        
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

label trainee_show:
    $ love = heroine_love['trainee']
    
    if love < 50000:
        show trainee_1
    elif love < 100000:
        show trainee_2
    else:
        show trainee_3
        
    return

label trainee_hide:
    hide trainee_1
    hide trainee_2
    hide trainee_3
    return
    
label trainee_teachers_room:
    $ a = random.randint(0, 3)
    
    call trainee_show
    
    if a == 0:
        call trainee_global_1
    if a == 1:
        call trainee_global_2
    if a == 2:
        call trainee_global_3
    if a == 4:
        call trainee_teachers_room_limit_1
    
    call trainee_hide
        
    return
         
label trainee_old_school:
    $ a = random.randint(0, 3)

    call trainee_show    

    if a == 0:
        call trainee_global_1
    if a == 1:
        call trainee_global_2
    if a == 2:
        call trainee_global_3
    if a == 4:
        call trainee_old_school_1
    
    call trainee_hide
        
    return
        
label trainee_security_office:
    $ a = random.randint(0,2)
   
    call trainee_show
    
    if a == 0:
        call trainee_global_1
    if a == 1:
        call trainee_global_2
    if a == 2:
        call trainee_global_3
    
    call trainee_hide
        
    return
  

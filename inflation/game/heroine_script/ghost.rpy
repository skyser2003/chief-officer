define ghost = Character("유령",color="#f00")
define A = Character("나", color="#000")

label ghost_global_1: #FIXME
    ghost  "%(hero_name)s야!"
    menu:
        "(B가 나를 부른 것 같다.)"
        "대답한다.":
            A   "응? 아 B구나"
            "B와 대화를 나누다 교실로 돌아갔다" 
            return
        "무시한다.":
            A  "(귀찮으니 그냥 가자)...."
            ghost   "와! 저 나를 무시하는 시크한 모습!.....멋져!"
            "B를 무시한체 교실로 돌아왔다"
            return
        "시비를 건다.":
            A "길가다 아무나 막 부르고 똥오줌 못가리지!"
            ghost "미....미안.... 반..가워서..."
            ghost "(저 강한 모습... 정말 멋져!)"
            ghost "겁에 질려있는것같은 B를 뒤로한채 교실로 돌아왔다"
                            
    return
    
label ghost_global_2: #FIXME
    menu:
        A "(어 B가 지나간다.)"
        "말을 건다.":
            A "B야!"
            ghost "어? A구나!"
            "B와 대화를 나누다 교실로 돌아갔다."
            return
        "무시한다.":
            A "(괜히 말걸면 귀찮으니깐 그냥 가자)"
        "삥을 뜯는다.":
            A "야 B! 돈좀 있냐?"
            ghost "드...드리겠습니다!"
            A "필요없어!"
            ghost "(어머 저 박력! 멋져!)"
            "돈을 가지고 교실로 돌아왔다"
        
    return
    
label ghost_global_3: #FIXME
    call ghost_hide
    A "아 귀찮다 그냥 자야지..,"
    "(그렇게 그는 생각하는 것을 그만두었다.)"
        
    return

label ghost_old_school_1: #FIXMEEEE
    "유령 - 구교사 공통 1"
    
    menu:
        "선택"
        "선택지1":
            pass
        "선택지2":
            pass
        "선택지3":
            pass
        
    return
    
label ghost_show:
    $ love = heroine_love['ghost']
    
    if love < 50000:
        show ghost_1
    elif love < 100000:
        show ghost_2
    else:
        show ghost_3
        
    return

label ghost_hide:
    hide ghost_1
    hide ghost_2
    hide ghost_3
    return

label ghost_security_office:
    $ a = random.randint(0, 0)
    
    call ghost_show
    
    if a == 0:
        call ghost_global_1
    if a == 1:
        call ghost_global_2
    if a == 2:
        call ghost_global_3
        
    call ghost_hide
        
    return
    
label ghost_old_school:
    $ a = random.randint(0, 3)
    
    call ghost_show
    
    if a == 0:
        call ghost_global_1
    if a == 1:
        call ghost_global_2
    if a == 2:
        call ghost_global_3
    if a == 3:
        call ghost_old_school_1

    call ghost_hide
        
    return


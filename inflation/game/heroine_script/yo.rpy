define yo = Character("요자",color="#000000")
define A = Character("나", color="#000")

label yo_global_1: #FIXME
    yo  "%(hero_name)s야!"
    menu:
        "(B가 나를 부른 것 같다.)"
        "대답한다.":
            A   "응? 아 B구나"
            "B와 대화를 나누다 교실로 돌아갔다" 
            return
        "무시한다.":
            A  "(귀찮으니 그냥 가자)...."
            yo   "와! 저 나를 무시하는 시크한 모습!.....멋져!"
            "B를 무시한체 교실로 돌아왔다"
            return
        "시비를 건다.":
            A "길가다 아무나 막 부르고 똥오줌 못가리지!"
            yo "미....미안.... 반..가워서..."
            yo "(저 강한 모습... 정말 멋져!)"
            yo "겁에 질려있는것같은 B를 뒤로한채 교실로 돌아왔다"
        
    return
    
label yo_global_2:  #FIXME   
    menu:
        A "(어 B가 지나간다.)"
        "말을 건다.":
            A "B야!"
            yo "어? A구나!"
            "B와 대화를 나누다 교실로 돌아갔다."
            return
        "무시한다.":
            A "(괜히 말걸면 귀찮으니깐 그냥 가자)"
            return
        "삥을 뜯는다.":
            A "야 B! 돈좀 있냐?"
            yo "드...드리겠습니다!"
            A "필요없어!"
            yo "(어머 저 박력! 멋져!)"
            "돈을 가지고 교실로 돌아왔다"
        
    return
    
label yo_global_3: #FIXME
    call yo_hide
    A "아 귀찮다 그냥 자야지..,"
    "(그렇게 그는 생각하는 것을 그만두었다.)"
        
    return

label yo_toilet_1: #FIXME
    A "화장실 급하다 급해!"
    "꽈당!"
    menu:
        yo '아야야'
        "미안해, 괜찮아?” (상냥해... 부앜)":
            yo "으응 괜찮아 덕분에..."
            A "그래 그럼 다행이구나"
            "B를 일어나켜준뒤 교실로 돌아왔다."
            return
        "어딜보고다녀 시밤바야? 니 눈은 장식이냐? (거친 남자 멋져 부와왘)":
            yo "미...미안해.."
            A "알면 됬어 다음부터 조심해"
            yo "저런...와일드한 모습...멋져!"
            "(넘어져있는 B를 뒤로한채 교실로 돌아왔다)"
            return
        
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

label yo_show:
    $ love = heroine_love['yo']
    
    if love < 50000:
        show yo_1
    elif love < 100000:
        show yo_2
    else:
        show yo_3
        
    return

label yo_hide:
    hide yo_1
    hide yo_2
    hide yo_3
    return

label yo_toilet:
    $ a = random.randint(0, 5)
    
    call yo_show
    
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
     
    call yo_hide    
        
    return


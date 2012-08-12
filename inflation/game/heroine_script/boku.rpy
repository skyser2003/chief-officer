define boku = Character("보쿠소녀",color="#FFFFFF")

label boku_global_1:
    A "(으아아아앙아 졸려...  교실 가서 잘까)"
    boku "저... 저기 안녕하세요?"
    
    menu:
        "보쿠소녀가 나를 부른 거 같다":
            A "응?  아 너구나.  안녕"
            "보쿠소녀와 대화를 나누다 교실로 돌아왔다"
            $ heroine_love['boku'] += 10000
            pass
        "무시한다":
            A "(귀찮으니 그냥 가자...)"
            call boku_hide
            show boku_2
            boku "와!  저 나를 무시하는 시크한 모습!  ...멋져!"
            "보쿠소녀를 무시한 채 교실로 돌아왔다"
            $ heroine_love['boku'] += 20000
            pass
        "시비를 건다":
            A "길가다가 아무나 막 부르고"
            "똥오줌 못 가리지!"
            boku "죄... 죄송해요...  정말 반가워서....."
            call boku_hide
            show boku_2
            boku "(저 강한 모습....  멋져!)"
            "겁에 질려 있는 것 같은 모습의 보쿠소녀를 뒤로 하고 교실로 돌아왔다"
            $ heroine_love['boku'] += 30000
            pass
        
    return
    
label boku_global_2:
    call boku_hide
    A "으아아아아아아 심심해 어디 지나가는 사람 없나"
    show boku_1
    A "엇 저기 보쿠소녀다 ㅇㅅㅇ"
    
    menu:
        "말을 건다":
            A "보쿠소녀야!"
            boku "어 안녕하세요~"
            "보쿠소녀와 대화를 나누다 교실로 돌아왔다"
            $ heroine_love['boku'] += 10000
            pass
        "무시한다":
            A "(괜히 말 걸면 귀찮으니까 그냥 가자)"
            pass
        "삥을 뜯는다":
            A "야!  보쿠소녀 너 돈 좀 있어?"
            boku "드... 드릴게요!"
            A "필요없어!"
            call boku_hide
            show boku_2
            boku "(어머 저 박력... 멋져!)"
            "돈을 가지고 교실로 돌아왔다"
            $ heroine_love['boku'] += 30000
            pass
        
    return
    
label boku_global_3:
    call boku_hide
    A "아 귀찮다 그냥 자야지..,"
    "(그렇게 그는 생각하는 것을 그만두었다.)"
    
    return

label boku_ground_1:
    "공이 날아온다"
    A "음? 이건 뭐지?"
    boku "저 그 공좀 던져주세요!"
    
    menu:
        "돌려준다":
            boku "감사합니다"
            "고마워하는 보쿠소녀를 뒤로하고 교실로 돌아왔다."
            $ heroine_love['boku'] += 10000
            pass
        "줏으면 내 거 아닌가?":
            boku "저..저기 그 공 가져가시면 안되요!"
            A "...."
            call boku_hide
            show boku_2
            boku "저..과묵함! 멋져!"
            "우연히 줏은 공을 가지고 기쁜마음으로 교실로 돌아왔다."
            $ heroine_love['boku'] += 20000
            pass
        "공에도 자유를!":
            A "자 볼! 자유를 향해 나아가!"
            boku "아..아 내공이!"
            A "오늘도 보람찬 일을 했군 그만 돌아가봐야지"
            call boku_hide
            show boku_2
            boku "저 무생물에게도 정을 쏟는 모습...멋져!!!"
            "뿌듯한 마음으로 교실로 돌아왔다."
            
            $ heroine_love['boku'] += 30000
            pass
        
    return

label boku_ground_2:
    "공이 날아와서 맞았다"
    A "앗! 이건 뼛속까지 아프다! , 어디서 날라온 공이지? 저긴가?"
    boku "아 정말 죄송합니다 괜찮으신가요?"
    
    menu:
        "남자면 이 정도는 참아야지":
            A "네 괜찮아요"
            boku "정말요? 세게 맞으신것 같은데.."
            A "아뇨 사실은 아파!"
            call boku_hide
            show boku_2
            boku "아니 이런 솔직함! 멋져!"
            "아픔을 참으며 교실로 돌아왔다"
            
            $ heroine_love['boku'] += 10000
            pass
        "주먹이 운다! 징징!":
            A "도륙을 내버릴까?"
            boku "아..안되!"
            A "되!"
            "퍽!"
            call boku_hide
            show boku_2
            boku "아니? 이 감각은!"
            "보쿠소녀를 보고 상태가 이상하다 생각해 황급히 교실로 돌아왔다"
            
            $heroine_love['boku'] += 30000
            pass
        
    return
       
label boku_ground_3:
    A " 혼자 운동장에 줄을 긋고있는 여자아이가 있다"
    menu:
        "여자아이를 혹사시킬순 없지, 가서 도와주자":
            A " 보쿠소녀야 내가 도와줄게"
            boku "정말? 고마워!"
            "(줄을 긋는걸 도와준뒤 교실로 돌아왔다.)"
            $ heroine_love['boku'] += 10000
            pass
        "자기의 일은 스스로하는 거지.":
            "쓸쓸히 자신의 일을 해내는 보쿠소녀의 모습을 묵묵히 응원하며 교실로 돌아왔다."
            pass
        
    return
       
label boku_ground_limit_1:
    "보쿠소녀 - 운동장 한정 1"
    A "어라 보쿠소녀잖아 야!"
    boku "오 오랜만이네 나와 승부하자!"
    menu:
        "그 승부 받아주지!":
            A "자 돌멩이를 몇개 던져봐라!"
            boku "이얍!"
            call boku_hide
            show boku_2
            "이럴수가 모두 피하다니.. 멋져!"
            A " 그럼 난 가봐야겠군 이만"
            call boku_hide
            show boku_1
            boku " 좋아! 다음에 다시 승부다!"
            " 연습에 열내고있는 보쿠소녀를 뒤로한체 교실로 돌아왔다."
            
            $ heroine_love['boku'] += 10000
            pass
        "여자아이와 승부할 순 없지":
            call boku_hide
            show boku_2
            boku "날 배려하는 그런모습... 감동이야!!"
            A "그럼 열심히 해"
            "교실로 돌아왔다."
            
            $ heroine_love['boku'] += 20000
            pass

label boku_show:
    $ love = heroine_love['boku']
    
    if love < 50000:
        show boku_1
    elif love < 100000:
        show boku_2
    else:
        show boku_3
        
    return

label boku_hide:
    hide boku_1
    hide boku_2
    hide boku_3
    return

label boku_gym:
    show boku_1
    $ a = random.randint(0, 2)
    
    if a == 0:
        call boku_global_1
    if a == 1:
        call boku_global_2
    if a == 2:
        call boku_global_3
      
    call boku_hide    
        
    return
          
label boku_ground:
    show boku_1
    $ a = random.randint(0, 6)
    
    if a == 0:
        call boku_global_1
    if a == 1:
        call boku_global_2
    if a == 2:
        call boku_global_3
    if a == 3:
        call boku_ground_1
    if a == 4:
        call boku_ground_2
    if a == 5:
        call boku_ground_3
    if a == 6:
        call boku_ground_limit_1
    
    call boku_hide    
        
    return
   

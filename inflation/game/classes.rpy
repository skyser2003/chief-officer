init:
    $ style.input.color = '#000'            
    screen hinput:
        add HangulInput('이름을 적어줘!', color='#000') align (.5, .5)

label opening:
    scene bg_opening
    play music "bgm/opening.mp3"
    
    call screen hinput
    $ hero_name, final = _return
    
    "만약 평생얻을 호감도를 이틀동안 얻게된다면!"
    "만나기만해도 호감도가 부왘!!"
    "본격 호감도 인플레 게임의 이일차가 시작되었다!"
    
    return
    
label first_class:
    scene bg_class
    play music "bgm/school1.mp3"
    "1교시, 쉬는시간"
    call activity
    return
    
label second_class:
    scene bg_class
    "2교시, 쉬는시간"
    call activity
    return
    
label third_class:
    scene bg_class
    "3교시, 쉬는시간"
    call activity
    return
    
label forth_class:
    scene bg_class
    "4교시, 점심시간"
    call activity
    call activity
    return
    
label fifth_class:
    scene bg_class
    "5교시, 쉬는시간"
    call activity
    return
    
label sixth_class:
    scene bg_class
    "6교시, 쉬는시간" 
    call activity      
    return
    
label seventh_class:
    scene bg_class
    "7교시"
    return


# baekansi@naver.com / 백안시 / 2011.7.13

init python:
    
    class HangulInput(renpy.Displayable):
        
        cho = jung = jong = 0

        def __init__(self, prompt = '', default = '', length = 100, allow=None, exclude='{}', style = 'default', **properties):
            renpy.Displayable.__init__(self, "", style = style, **properties)
            
            self.ptext = unicode(prompt)
            self.prompt = Text(prompt, style = style, **properties)
            self.content = unicode(default)
            
            self.length = length
            self.allow = allow
            self.exclude=  exclude
            self.caret = unicode('')
            
            self.state = 'start'
            
        def flush(self):
            self.content = self.content + self.caret
            self.caret = ''
            self.update_text(self.content, self.caret)
            
            self.cho = self.jung = self.jong = 0
            self.state = 'start'

        def done(self):
            import re
            self.flush()
            final = False
            temp = self.content
            expr = re.compile(r'([a-zA-Z0-9\s~!@#$%^&*()_+|}{:"<>?`\-=\\\[\];\',./])')
            temp = expr.sub('', temp)
            if temp == '':
                return self.content, final
                
            last_alphabet = repr(temp[-1])
            dec = int(str(last_alphabet[4:-1]), 16)
                
            while dec < 0x3164:
                temp = temp[:-1]
                if not temp:
                    final = False
                    return self.content, final
                    
                last_alphabet=repr(temp[-1])
                dec = int(str(last_alphabet[4:-1]), 16)
                
            dec= (dec-44032) % 588 % 28
            
            if dec == 0: 
                final = False
            else: 
                final = True
        
            return self.content, final
            
        def etoh(self, state, input):
            choseongs = (0, 1, 3, 6, 7, 8, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29)
            choseongValue = (1, 2, 3, 4, 5, 6, 7,  8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)    
                                    # ㄱ ㄲ ㄴ ㄷ ㄸ ㄹ ㅁ ㅂ ㅃ ㅅ ㅆ ㅇ ㅈ ㅉ ㅊ ㅋ ㅌ ㅍ ㅎ
            jungseongs = (30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50)
                                # ㅏㅐ ㅑ ㅒ ㅓ ㅔ ㅕ ㅖ ㅗ ㅘ ㅙ ㅚ ㅛ ㅜ ㅝ ㅞ ㅟ ㅠ ㅡ ㅢ ㅣ
            jungseongValue = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)
            jungseong_pairs = ((9, 30), (9, 31), (9, 50), (14, 34), (14, 35), (14, 50), (19, 50))

            jongseong_pairs = ((1, 20), (4, 23), (4, 29), (8, 0), (8, 16), (8, 17), (8, 20), (8, 27), (8, 28), (8, 29), (17, 20)) 
            
            input = int(input)
            
            if state=='start':             # 아무 글자도 없을때
            
                self.caret = unichr(0x3131+input)
                
                if input <30:
                    self.state='choseong'
                    self.cho = self.choose(input, choseongs, choseongValue)
                    
                elif input >= 30:
                    self.flush()
                        
            elif self.state == 'choseong':        # ㄱ을 눌렀을 때
                
                if input <30:  # 또 자음을 누르면
                    if len(self.content)+1 <self.length:
                        self.content = self.content + self.caret
                        self.caret = unichr(0x3131 + input)
                        
                        self.cho = self.choose(input, choseongs, choseongValue)

                elif input >=30 and not (input in (38, 43, 48)):      # 모음을 눌렀는데 조합되는 종성이 아니라면
                    self.jung = self.choose(input, jungseongs, jungseongValue)
                    self.caret = (self.cho-1) * 588 + (self.jung-1)*28 + 44032
                    self.caret = unichr(self.caret)
                    self.state = 'jungseong'
                    
                elif input in (38, 43, 48):    # 모음을 눌렀는데 조합되는 종성이라면
                    self.jung = self.choose(input, jungseongs, jungseongValue)
                    self.caret = unichr((self.cho-1) * 588 + (self.jung-1)*28 + 44032)
                    self.state = 'jungseong2'
                    

            elif self.state == 'jungseong' or self.state == 'jungseong3':   # 중성이 있을 때 기, 과
                
                self.temp = self.caret
                
                if input in (0, 3, 8, 17):         # 종성 조합 가능한 자음을 누르면: 길
                    self.jong = self.choose(input, choseongs, (1, 2, 4, 7, 0, 8, 16, 17, 0, 19, 20, 21, 22, 0, 23, 24, 25, 26, 27))
                    self.caret = unichr( (self.cho-1) * 588 + (self.jung-1)*28 + self.jong + 44032 )
                    self.state = 'jongseong2'
                    
                elif input in (7, 18, 24):     # 받침으로 올 수 없는 글자를 누르면: 기ㅉ
                    if len(self.content)+1<self.length:
                        self.content = self.content + self.caret
                        self.cho = self.choose(input, choseongs, choseongValue)
                        self.caret = unichr(0x3131 + input)
                        self.state = 'choseong'
                    
                elif input >=30:   # 모음을 누르면 처음으로 돌아감: 기ㅣ
                    if len(self.content)+1<self.length:
                        self.content = self.content + self.caret
                        self.caret = unichr(0x3131 + input)
                        self.flush()
                    
                else:       # 자음을 누르면: 김
                    self.jong = self.choose(input, choseongs, (1, 2, 4, 7, 0, 8, 16, 17, 0, 19, 20, 21, 22, 0, 23, 24, 25, 26, 27))
                    self.caret = unichr( (self.cho-1) * 588 + (self.jung-1)*28 + self.jong + 44032 )
                    self.state = 'jongseong'
                    
                    
            elif self.state == 'jungseong2':  # 조합 가능한 중성이 입력 중일때: 구
                self.temp = self.caret
                
                if (self.jung, input) in jungseong_pairs:       # 조합 가능한 모음을 입력하면: 궈
                    
                    jungComb = (10, 11, 12, 15, 16, 17, 20)        
                    
                    self.jung = jungComb[self.choose_index((self.jung, input), jungseong_pairs)]
                    
                    self.caret =  unichr( (self.cho-1) * 588 + (self.jung-1)*28 + 44032 )
                    self.state = 'jungseong3'

                elif input < 30:    # 자음을 입력하면 
                    
                    if input in (0, 3, 8, 17):         # 종성 조합 가능한 자음을 누르면 국
                        self.jong = self.choose(input, choseongs, (1, 2, 4, 7, 0, 8, 16, 17, 0, 19, 20, 21, 22, 0, 23, 24, 25, 26, 27))
                        self.caret = unichr( (self.cho-1) * 588 + (self.jung-1)*28 + self.jong + 44032 )
                        self.state = 'jongseong2'

                    elif input in (7, 18, 24):      # ㄸㅉ같은 거 누르면 구ㅉ
                        if len(self.content)+1<self.length:
                            self.content = self.content + self.temp
                            self.cho = self.choose(input, choseongs, choseongValue)
                            self.caret = unichr(0x3131 + input)
                            
                            self.state = 'choseong'
                            
                    else:       # 자음을 누르면 궇
                        self.jong = self.choose(input, choseongs, (1, 2, 4, 7, 0, 8, 16, 17, 0, 19, 20, 21, 22, 0, 23, 24, 25, 26, 27))
                        self.caret = unichr( (self.cho-1) * 588 + (self.jung-1)*28 + self.jong + 44032 )
                        
                        if len(self.content)+1<self.length:
                            self.state = 'jongseong'
                            
                        else:
                            self.flush()

                elif input >= 30:  # 모음을 누르면
                    if len(self.content)+1<self.length:
                        self.content = self.content + self.caret
                        self.caret = unichr (0x3131 + input)
                        self.flush()
                        
                        
            elif self.state == 'jongseong':   # 종성이 있을 때  길
                if len(self.content)+1<self.length:
                    if input >= 30:    # 모음을 누르면
                        
                        self.content = self.content + self.temp      # 이전에 저장해뒀던 글씨를 content에 저장하고
                        self.cho = self.choose(self.jong, (1, 2, 4, 7, 0, 8, 16, 17, 0, 19, 20, 21, 22, 0, 23, 24, 25, 26, 27), choseongValue)
                        
                        if input in (38, 43, 48):  # 기루
                            self.jung = self.choose(input, jungseongs, jungseongValue)                
                            self.caret = unichr((self.cho-1) * 588 + (self.jung-1)*28 + 44032)
                            
                            self.state = 'jungseong2'      
                                        
                        else:
                            self.jung = self.choose(input, jungseongs, jungseongValue)
                            self.caret = unichr((self.cho-1) * 588 + (self.jung-1)*28 + 44032)
                            self.state = 'jungseong'
                        
                    elif input < 30:   # 자음을 누르면
                        
                        self.content = self.content +self.caret
                        self.cho = self.choose(input, choseongs, choseongValue)
                        self.caret = unichr(0x3131 + input)
                        self.state = 'choseong'
                        
                
            elif self.state == 'jongseong2':  # 조합 가능한 종성이 있을 때 각
                
                if (self.jong, input) in jongseong_pairs:       # 현재 종성과 조합 가능한 자음을 누르면 갃
                    
                    self.temp = self.caret
                    self.temp2 = input
                    
                    jongComb = (3, 5, 6, 9, 10, 11, 12, 13, 14, 15, 18)
                    self.jong = jongComb[self.choose_index((self.jong, input), jongseong_pairs)]
                    self.caret = unichr((self.cho-1) * 588 + (self.jung-1)*28 + self.jong + 44032)
                    self.state = 'jongseong3'
                    
                elif input < 30 and not ((self.jong, input) in jongseong_pairs):    # 그런거 아니고 그냥 자음을 누르면  각ㄴ  
                    if len(self.content)+1<self.length:
                        self.content = self.content + self.caret
                        self.cho = self.choose(input, choseongs, choseongValue)
                        self.caret = unichr(0x3131 + input)
                        
                        self.state = 'choseong'
                        
                elif input >= 30:       # 모음을 누르면 ex) 각 상태에서 모음 
                    if len(self.content)+1<self.length:
                        self.content = self.content + self.temp
                        self.cho = self.choose(self.jong, (1, 2, 4, 7, 0, 8, 16, 17, 0, 19, 20, 21, 22, 0, 23, 24, 25, 26, 27), choseongValue)
                        
                        if input in (38, 43, 48):      # 조합 가능한 글자면 가고
                            
                            self.jung = self.choose(input, jungseongs, jungseongValue)                
                            self.caret = unichr((self.cho-1) * 588 + (self.jung-1)*28 + 44032)
                            
                            self.state = 'jungseong2'      
                                        
                        else:      # 조합 불가능한 글자면 가게
                            
                            self.jung = self.choose(input, jungseongs, jungseongValue)
                            self.caret = unichr((self.cho-1) * 588 + (self.jung-1)*28 + 44032)
                            
                            self.state = 'jungseong'
                 

            elif self.state == 'jongseong3':  # 갃일 때
                if len(self.content)+1<self.length:
                    if input <30:      #자음을 눌렀다
                        self.content = self.content + self.caret
                        self.cho = self.choose(input, choseongs, choseongValue)
                        self.caret = unichr(0x3131 + input)
                        self.state = 'choseong'
                        
                    elif input in (38, 43, 48):    # 조합 가능한 모음을 눌렀다.
                        
                        self.content = self.content + self.temp
                        self.cho = self.choose(self.temp2, choseongs, choseongValue)
                        self.jung = self.choose(input, jungseongs, jungseongValue)                
                        self.caret = unichr((self.cho-1) * 588 + (self.jung-1)*28 + 44032)
                        
                        self.state = 'jungseong2'
                        
                    elif input >= 30:          # 그냥 모음을 눌렀다. 그러면 ㄱ 랑 ㅅ 랑 분리되어야 함. 각사
                        self.content = self.content + self.temp
                        self.cho = self.choose(self.temp2, choseongs, choseongValue)
                        self.jung = self.choose(input, jungseongs, jungseongValue)
                        self.caret = (self.cho-1) * 588 + (self.jung-1)*28 + 44032
                        self.caret = unichr(self.caret)
                        self.state = 'jungseong'
                        
        def choose(self, key, array, array2):
            for i, k in enumerate(array):
                    if key == k:
                            return array2[i]
            return None
                
        def choose_index(self, key, array):
            for i, k in enumerate(array):
                    if key == k:
                            return i
            return None
            
        def atov(self, alphabet):
            dict = {'r':0, 'R':1, 's':3, 'e':6, 'E':7, 'f':8, 'F':8, 'a':16, 'q':17, 'Q':18, 't':20, 'T':21, 'd':22, 'w':23, 'W':24, 'c':25, 'z':26, 'x':27, 'v':28, 'g':29, 
                    # 자음 ㄱ ㄲ ㄴ ㄷ ㄸ ㄹ ....
            'k':30, 'o':31, 'i':32, 'O':33, 'j':34, 'p':35, 'u':36, 'P':37, 'h':38, 'y':42, 'n':43, 'b':47, 'm':48, 'l':50
                # 모음 ㅏ ㅐ ㅒ ㅓ ㅔ ㅕ ㅖ ....
                }
            if dict.has_key(alphabet):
                v = dict[alphabet]
                return v
            else:
                return alphabet
                
        def update_text(self, content, caret):
            renpy.redraw(self, 0)
            
            if content != self.content:
                self.content = content
            if caret != self.caret:
                self.caret = caret
                
        def render(self, width, height, st, at):
            
            pw = ph = 0
            
            if self.ptext:
                prompt = renpy.render(self.prompt, 800, 600, st, at)
                pw, ph = prompt.get_size()
            
            if self.caret:
                self.text = Text('%s{u}%s{/u}' %(self.content, self.caret), style = 'input')
            else:
                self.text = Text('%s|' %(self.content), style = 'input')
            
            text = renpy.render(self.text, 800, 600, st, at)
            tw, th = text.get_size()
            
            r = renpy.Render(pw+ tw, ph + th)
            
            if self.ptext:
                r.blit(prompt, (0, 0))
                
            r.blit(text, (0, ph))
            return r
            

        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                self.flush()
                final = 0
                if self.content:
                    self.content, final = self.done()
                return self.content, final
            
            elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_BACKSPACE:
                if self.caret:
                    self.caret = unicode('')
                    self.state = 'start'
                else:
                    self.content = self.content[:-1]
                        
                renpy.redraw(self, 0)
                
            elif ev.type is pygame.KEYDOWN and ev.unicode:
                
                if ord(ev.unicode[0]) <32:
                    return None
                
                if self.length and len(self.content) >= self.length:
                    raise renpy.IgnoreEvent()
                    
                if self.allow and ev.unicode not in self.allow:
                    raise renpy.IgnoreEvent()
                    
                if self.exclude and ev.unicode in self.exclude:
                    raise renpy.IgnoreEvent()
                    
                else:
                    result = self.atov(ev.unicode)
                    
                    if result <= 50:
                        self.etoh(self.state, result)
                        
                    elif (result >= 'a' and result <='z') or (result >= 'A' and result <= 'Z'):
                        raise renpy.IgnoreEvent()
                        
                    else:
                        self.flush()
                        self.content = self.content + ev.unicode
                        
                    
                self.update_text(self.content, self.caret)
                
                raise renpy.IgnoreEvent()
        
class Star:
    name = 'Star' # class 변수
    x = 100 # class 변수

    def chage():
        x = 200
        print('x is', x)


print('x is', Star.x) #클래스 변수 엑세스
Star.chage() # 클래스 함수

star = Star() # 생성자가 없는데 생성
print(type(star))
print(star.x) #비록 객체 변수로 액세스했으나, 같은 이름의 클래스 변수가 우선

star.chage() # Star.cahge(star) 와 동일
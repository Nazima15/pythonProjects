class Circle:  
    def __init__(self, r):
        # self.__radius -> 힙(Heap)에 저장되는 인스턴스 변수 (private)
        self.__radius = r

    def setRadius(self, r):
        # __radius 값을 바꿀 수 있는 setter
        self.__radius = r

    def getRadius(self):
        # __radius 값을 가져오는 getter
        return self.__radius

    def __str__(self):
        # 객체를 문자열로 표현할 때 호출됨
        # (여기서는 오류 있음: self.radius → self.__radius 로 바꿔야 정상 동작)
        return "r=%f" % (self.__radius)


# c1 = Circle(1.0)
# 1) Circle 객체가 힙(Heap)에 생성됨
# 2) __radius = 1.0 저장
# 3) 스택(Stack)에 변수 c1 생성, 힙의 객체 주소 저장
c1 = Circle(1.0)

# c1 = c2
# 스택에서 c1이 원래 가리키던 객체 주소를 버리고,
# c2가 가리키는 같은 객체를 가리키게 됨 (주소 복사)
c2 = Circle(5.0)
c1 = c2   # 이제 c1과 c2는 같은 객체를 가리킴

# c1.__radius = 2.0  # ❌ ERROR (private 변수라서 직접 접근 불가)

# setter를 사용해야 함
c1.setRadius(2.0)   # ⭕ OK, __radius = 2.0 으로 변경됨

# print(c1.__radius)  # ❌ ERROR (외부에서 직접 접근 불가)

# getter 사용
print(c1.getRadius())  # ⭕ OK, 출력: 2.0

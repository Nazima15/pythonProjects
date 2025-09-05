class Circle:  # 원을 나타내는 Circle 클래스 정의
    def __init__(self, r):  # 객체가 생성될 때 호출되는 초기화 메서드
        self.__radius = r   # 반지름 값을 비공개 변수로 저장

    def getArea(self):  # 원의 넓이를 계산하는 인스턴스 메서드
        return 3.14 * self.__radius ** 2  # 넓이 공식(πr²) 반환

    @staticmethod
    def getInfo():  # 정적 메서드: 클래스나 객체 정보에 접근하지 않음
        return "Circle"  # 단순히 "Circle" 문자열 반환

    @classmethod
    def getInfo2(cls, r):  # 클래스 메서드: 클래스 자체를 첫 번째 인자로 받음
        return cls(r)      # 전달받은 r로 Circle 객체를 생성해 반환

print(Circle.getInfo())  # 클래스명으로 정적 메서드 호출 ("Circle" 출력)
c1 = Circle(1.0)         # 반지름이 1.0인 Circle 객체 생성
print(c1.getArea())      # c1 객체의 넓이 출력 (3.14)
c2 = Circle.getInfo2(10) # 클래스 메서드로 반지름 10인 Circle 객체
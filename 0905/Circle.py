class Circle:  # 원을 나타내는 Circle 클래스(설계도)를 정의합니다.
    def __init__(self, r):  # 객체가 생성될 때 자동으로 호출되는 초기화 메서드입니다.
        self.radius = r  # 전달받은 r 값을 객체의 radius(반지름) 속성에 저장합니다.
    def area(self):  # 원의 넓이를 계산하는 메서드입니다.
        return 3.14 * self.radius ** 2  # 원의 넓이 공식(πr²)을 사용하여 값을 반환합니다.
    def perimeter(self):  # 원의 둘레를 계산하는 메서드입니다.
        return 2 * 3.14 * self.radius  # 원의 둘레 공식(2πr)을 사용하여 값을 반환합니다.
    def __str__(self):  # 객체를 문자열로 표현할 때 호출되는 메서드입니다.
        # 반지름, 넓이, 둘레 값을 문자열로 만들어 반환합니다.
        return "r=%f area=%f perimeter=%f" % (self.radius, self.area(), self.perimeter())
    
c1 = Circle(1.0)  # 반지름이 1.0인 Circle 객체를 생성합니다.
print(c1)  # c1 객체를 출력하면 __str__ 메서드가 자동으로 호출되어 정보가
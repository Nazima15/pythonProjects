class Box:  # Box라는 이름의 클래스(설계도)를 정의합니다.
    def __init__(self, w, h):  # 객체가 생성될 때 자동으로 호출되는 초기화 메서드입니다.
        self.width = w         # 전달받은 w 값을 객체의 width(가로) 속성에 저장합니다.
        self.height = h        # 전달받은 h 값을 객체의 height(세로) 속성에 저장합니다.
    def area(self):            # Box 객체의 넓이를 계산하는 메서드입니다.
        return self.width * self.height  # 가로 * 세로 값을 반환합니다.
    
myBox = Box(2, 3)  # Box 클래스의 인스턴스를 만들고, 가로 2, 세로 3을 전달합니다.
print('가로=%d, 세로=%d' % (myBox.width, myBox.height))  # myBox의 가로와 세로 값을 출력합니다.
print(myBox.area())  # myBox의 넓이(2*3)
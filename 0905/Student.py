class Student:  # Student라는 이름의 클래스(설계도)를 정의합니다.
    def __init__(self, name="student"):  # 객체가 생성될 때 자동으로 호출되는 초기화 메서드입니다.
        self.name = name  # 전달받은 name 값을 객체의 name(이름) 속성에 저장합니다.
    def Hello(self):  # Student 객체의 인사 메서드입니다.
        print("Hello", self.name)  # 객체의 name 값을 이용해 인사말을 출력합니다.

s1 = Student("user")  # Student 클래스의 인스턴스를 만들고, 이름에 "user"를 전달합니다.
                      # 1. Student 객체가 생성됨
                      # 2. __init__ 메서드가 자동으로 호출되어 name 속성에 "user"가 저장됨
s1.Hello()  # s1 객체의 Hello 메서드를 호출하여 "Hello user"를
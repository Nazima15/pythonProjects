class Shape:
    def __init__(self):
        self.name = "Shape"

class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.name = "Circle"
        self.radius = 0
c1=Circle()
print(c1.name)  # Circle
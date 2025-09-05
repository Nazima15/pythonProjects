class Circle:  
    def __init__(self, r):
        self.__radius = r
    def setRadius(self, r):
        self.__radius = r
    def getRadius(self):
        return self.__radius
    def __str__(self):
        return "r=%f area=%f perimeter=%f" % (self.radius, self.area(), self.perimeter())
    
c1=Circle(1.0)
#c1.__radius=2.0 ERROR
c1.setRadius(2.0)
#print(c1__radius) ERROR
print(c1.getRadius()) #OK
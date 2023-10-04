class Square:
    def __init__(self,sideLength):
        self.length = sideLength
        
    def area(self):
        return self.length**2
        
    def perimeter(self):
        return self.length*4
        
    def printAreaPerim(self):
        myArea = self.area()
        myPerimeter = self.perimeter()
        print(f"The area is {myArea} and the perimeter is {myPerimeter}")
    
    
square1 = Square(5)
square1.printAreaPerim()

square2 = Square(2)
square2.printAreaPerim()

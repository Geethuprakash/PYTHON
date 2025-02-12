class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return (self.length * self.breadth)
    def perimeter(self):
        return(2*(self.length+self.breadth))

    def compare(self, other):
        if self.area() == other.area():
            print("area of both rectangle are equal")
        else:
            print("area of both rectangle are not equal")

r1 = Rectangle(10,20)
r2 = Rectangle(50,5)


print(f"Area of First rectangle is : {r1.area()}")
print(f"Perimeter of First rectangle is : {r1.perimeter()}")
print(f"Area of Second rectangle is : {r2.area()}")
print(f"Perimeter of Second rectangle is : {r2.perimeter()}\n")
r1.compare(r2)

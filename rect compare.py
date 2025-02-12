class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.area() < other.area()


rect1 = Rectangle(4, 5)
rect2 = Rectangle(6, 3)

if rect1 < rect2:
    print("Rectangle 1 is smaller than Rectangle 2.")
else:
    print("Rectangle 1 is not smaller than Rectangle ")
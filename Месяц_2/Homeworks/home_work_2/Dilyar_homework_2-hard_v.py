# home work hard version
class Figure:
    unit = 50
    def __init__(self, cm):
        self.__calculate_perimeter()
        self.calculate_area()
        self.unit = cm

    def perimeter(self, __perimeter=0):
        self.premieter = __perimeter

    def get_perimeter(self):
        return self.perimeter

    def set_perimeter(self, perimeter):
        self.perimeter = perimeter

    def __str__(self):
        pass

    def calculate_area(self):
        print("Calculate Area")

    def __calculate_perimeter(self):
        print("Calculate Perimeter")

    def info(self):
        pass

class Square(Figure):
    def __init__(self, __side_length):
        self.__side_length = __side_length
        self.calculate_area()
        self.perimeter = self.__calculate_perimeter()

    def calculate_area(self):
        return f"Square: {self.__side_length * 2}"

    def __calculate_perimeter(self):
        return f"Perimeter: {self.__side_length * 4}"

    def info(self):
        print(f"SQUARE: Side length:{self.__side_length} Area:{self.calculate_area()} Perimeter:{self.__calculate_perimeter()}")

class Rectangle(Figure):
    def __init__(self, __length, __width):
        self.__width = __width
        self.__length = __length

    def calculate_area(self):
        return self.__length * self.__width

    def __calculate_perimeter(self):
        return (self.__length + self.__width) * 2

    def info(self):
        print(f"RECTANGLE: Length:{self.__length}cm Width:{self.__width}cm Perimeter:{self.__calculate_perimeter()}cm Area:{self.calculate_area()}cm ")

square1 = Square(5)
square2 = Square(9)

rectengle1 = Rectangle(1, 3)
rectengle2 = Rectangle(7, 9)
rectengle3 = Rectangle(4, 8)


rectengles = [rectengle1, rectengle2, rectengle3]
squares = [square1, square2]

for i in rectengles:
    i.info()

for k in squares:
    k.info()
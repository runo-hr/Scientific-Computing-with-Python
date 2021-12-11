class Rectangle:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

    def set_width(self, width ):
        self.width = width
        return print(f"width set to {self.width}")

    def set_height(self, height):
        self.height = height
        return print(f"height set to {self.height}")

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) **  .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ( '*' * self.width + '\n') * self.height

    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side = 0):
       # super().__init__(side, side)
        super(Square,self).__init__(side, side)
    def set_side(self, length):
        super().set_width(length)
        super().set_height(length)
    def set_height(self, height):
        super().set_height(height)
        super().set_width(height)
    def set_width(self, width):
        super().set_height(width)
        super().set_width(width)
    def __str__(self):
        return f"Square(side={self.width})"

myRectangle = Rectangle(4, 8)
#print(myRectangle.get_picture())
mySquare = Square()
mySquare.set_side(4)
#print(myRectangle.get_amount_inside(mySquare))
print(mySquare.get_area())
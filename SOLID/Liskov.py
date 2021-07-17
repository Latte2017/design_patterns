class Rectangle:
    def __init__(self) -> None:
        self._width = 0
        self._height = 0

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    
    @property
    def area(self):
        return self._height * self._width

class Square(Rectangle):

    @Rectangle.height.setter
    def height(self, value):
        self._height=value
        self._width=value

    @Rectangle.width.setter
    def width(self, value):
        self._height=value
        self._width=value

    
#Square class violates the liskov principle by setting height and width
# Better this is have a base class shape and derive rectangle and square from it 
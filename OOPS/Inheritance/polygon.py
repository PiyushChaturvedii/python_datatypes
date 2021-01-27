class Polygon:
    __width = None
    __height = None
    def set_value(self,  width, height):
        self.__height = height
        self.__width = width
    def get_width(self):
        return self.__width 
    def get_height(self):
        return self.__height


class Rectangle(Polygon):
    def area(self):
        return (self.get_width() * self.get_height())


rect = Rectangle()
tri = Triangle()
rect.set_value(50, 40)
tri.set_value(50, 40)
print(rect.area())
print(tri.area())
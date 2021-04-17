from rectangle import Rectangle
from triangle import Triangle

rect = Rectangle()
tri = Triangle()

rect.set_value(50, 50)
tri.set_value(50, 50)

tri.set_color('red')
rect.set_color('black')




print(tri.get_color())
print(rect.get_color())

print(rect.area())
print(tri.area())

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def set_width(self, width):
#         self.width = width
#
#     def set_height(self, height):
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
# class Square(Rectangle):
#     def __init__(self, size):
#         self.width = size
#         self.height = size
#
#     def set_width(self, width):
#         self.width = width
#         self.height = width
#
#     def set_height(self, height):
#         self.width = height
#         self.height = height
# ----------------------------------------------------------------

class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.height * self.width


class Square(Shape):
    def __init__(self, size):
        self.size = size

    def set_size(self, size):
        self.size = size

    def area(self):
        return self.size ** 2

def print_area(shape):
    print(f"Area: {shape.area()}")

if __name__ == '__main__':
    shapes = [Rectangle(5, 10), Square(7)]
    for shape in shapes:
        print_area(shape)

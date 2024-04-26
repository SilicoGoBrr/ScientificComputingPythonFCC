class Rectangle:
    def __init__ (self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        pic = '*' * self.width + '\n'
        pic = pic * self.height
        return pic

    def get_amount_inside (self, shape2):
        width_fit = (self.width // shape2.width)
        height_fit = (self.height // shape2.height)
        return width_fit * height_fit

    def __str__ (self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__ (self, side):
        super().__init__(side, side)
    
    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side

    def length(self, side):
        self.width = side
        self.height = side

    def __str__ (self):
       return f"Square(side={self.height})"

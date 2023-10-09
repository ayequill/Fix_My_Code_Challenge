#!/usr/bin/python3
""" Module for a square class """


class Square:
    """ A square class """
    # width = 0
    # height = 0

    def __init__(self, width=0, height=0):
        """ Constructor """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.width * 2)

    def __str__(self):
        """ String representation """
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":
    """ Create a square instance """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())

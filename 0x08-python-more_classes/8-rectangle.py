#!/usr/bin/python3
"""
This defines the "Rectangle" module.

This module provides a simple Rectangle class.
"""


class Rectangle:
    """
    A Rectangle class with attributes witdth and height,

    and methods area and perimeter, str, print, repr, and del and
    class attribute number_of_instances to keep track of
    number of instances, and class attribute print_symbol used as symbol for
    string representation while printing, and static method bigger_or_equal.
    It returns biggest rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        total = ""
        if self.__height == 0 or self.width == 0:
            return total
        for i in range(self.__height):
            for j in range(self.__width):
                try:
                    total += str(self.print_symbol)
                except Exception:
                    total += type(self).print_symbol
            if i != self.__height - 1:
                total += "\n"
        return total

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

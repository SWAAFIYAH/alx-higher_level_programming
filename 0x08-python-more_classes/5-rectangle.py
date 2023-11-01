#!/usr/bin/python3
"""Defineing Rectangle class."""

class Rectangle:
    """Representing rectangle."""

    def __init__(self, width=0, height=0):
        """Initializing new Rectangle.

        Args:
            width (int):  width of the new rectangle.
            height (int):  height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/sets width of the Rectangle."""
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
        """Get/sets height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns printable representation of the Rectangle.

        Representing rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for x in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if x != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Returning string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Printing message for every deletion of a Rectangle."""
        print("Bye rectangle...")

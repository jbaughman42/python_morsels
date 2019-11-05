"""
circle
Created November 05, 2019 by Jennifer Baughman

Description:
"""
import math


class Circle:
    def __init__(self, radius=1):
        self._radius = radius
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def diameter(self):
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
    
    @property
    def area(self):
        return math.pi * self.radius ** 2
    
    @area.setter
    def area(self, value):
        raise AttributeError
    
    def __str__(self):
        return f"Circle({self.radius})"

    def __repr__(self):
        return f"Circle({self.radius})"


if __name__ == "__main__":
    c = Circle(2)
    print(repr(c))
    c.radius = 1
    print(c.radius)
    print(c.diameter)
    print(c.area)

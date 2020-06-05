# file: circles.py
import math
from typing import Dict, List, Tuple, Union


def safe_radius_of(number: Union[int, float]) -> Union[int, float]:
    """ Function performs validation: checks if provided radius is of int or float type and > 0 """
    if not (
            isinstance(number, int) or
            isinstance(number, float)
    ):
        raise TypeError('Radius should be either "int" or "float" data type!')
    if number < 0:
        raise ValueError('Radius value should be more that "0"!')
    return number


def calculate_square_of(number: Union[int, float]) -> Union[int, float]:
    """ Function accepts either int or float number and returns its square """
    return number ** 2


def multiply_by_pi(number: Union[int, float]) -> Union[int, float]:
    """ Function accepts either int or float number and returns number multiplied by Pi """
    return math.pi * number


def double_of(number: Union[int, float]) -> Union[int, float]:
    """ Function accepts either int or float number and returns number multiplied by 2 """
    return number * 2


class Circle:
    def __init__(self, identifier: int, radius: Union[int, float], color: str) -> None:
        self.identifier = identifier
        self._radius = lambda: safe_radius_of(radius)
        self._color = color
    
    def change_color(self, color: str) -> None:
        """
        Method accepts color name in string format and updates the _color attribute of given
        Circle instance
        """
        if not isinstance(color, str):
            raise TypeError('Color should be "str" data type!')
        self._color = color
    
    def diameter(self) -> Union[int, float]:
        """ Method calculates the diameter for the given Circle instance """
        return double_of(self._radius())
    
    def area(self) -> float:
        """ Method calculates the area for the given Circle instance """
        return multiply_by_pi(calculate_square_of(self._radius()))
    
    def perimeter(self) -> Union[int, float]:
        """ Method calculates the perimeter for the given Circle instance """
        return double_of(multiply_by_pi(self._radius()))
    
    def __str__(self) -> str:
        """ Method returns info: radius and color for the given Circle instance """
        return f'Circle(radius={self._radius()}, color="{self._color}")'


class Circles:
    def __init__(self, *circles: Circle) -> None:
        self._circles = circles
    
    def update_colors(self, new_colors: Dict[int, str]) -> None:
        """
        Method accepts dict[identifier, new color], locates Circle instance with corresponding
        identifier and updates its color to new color provided 
        """
        for identifier, color in new_colors.items():
            this = self.find(identifier)
            this.change_color(color)

    def find(self, identifier: int) -> Circle:
        """ 
        Method locates the Circle instance with provided identifier and returns it.
        Exception is raised if no Circle instance was found in _circles attribute
        """
        for this in self._circles:
            if this.identifier == identifier:
                return this
        raise ValueError(f"There is no circle with this identifier: {identifier}")
    
    def show_diameters(self) -> None:
        """Method shows diameters for existing Circle instances"""
        for circle in self._circles:
            print(f"A diameter of {circle} is {circle.diameter()}")
    
    def show_areas(self) -> None:
        """Method shows areas for existing Circle instances"""
        for circle in self._circles:
            print(f"An area of {circle} is {circle.area():.2f}")
    
    def show_perimeters(self) -> None:
        """Method shows perimeters for existing Circle instances"""
        for circle in self._circles:
            print(f"A perimeter of {circle} is {circle.perimeter():.2f}")
  

if __name__ == "__main__":
    circles = Circles(
        Circle(1, 1, 'red'),
        Circle(2, 0.2, 'super-red'),
        Circle(3, 3, 'green'),
        Circle(4, 5, 'super-green'),
    )
    circles.show_diameters()
    circles.show_areas()
    circles.show_perimeters()
    circles.update_colors({
        1: 'blue',
        2: 'red',
        3: 'black',
        4: 'purple'
    })
    circles.show_diameters()
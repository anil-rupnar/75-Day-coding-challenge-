"""
Problem statement :
    write  a program to find area of circle when Diameter is given.
    Input : any positive integer denoting Diameter.
    Output : area of circle with two precision points.

"""

import math

def area_of_circle(diameter):
  radius = diameter / 2
  area = math.pi * radius * radius
  return area

diameter = int(input("enter the Diameter:"))
area = area_of_circle(diameter)
print(f"The area of the circle is: {area:.2f}")
from Triangle import Triangle
from Rectangle import Rectangle
from Trapezoid import Trapeze
from Parallelogram import Parallelogram
from Circle import Circle

shapes = []
with open('input02.txt', 'r') as file:
    for line in file:
        shape = line.strip().split( )
        shape_name = shape[0]
        if shape_name == 'Triangle':
            shapes.append(Triangle(int(shape[1]), int(shape[2]), int(shape[3])))
        elif shape_name == 'Rectangle':
            shapes.append(Rectangle(int(shape[1]), int(shape[2])))
        elif shape_name == 'Trapeze':
               shapes.append(Trapeze(int(shape[1]), int(shape[2]), int(shape[3]), int(shape[4])))
        elif shape_name == 'Parallelogram':
            shapes.append(Parallelogram(int(shape[1]), int(shape[2]), int(shape[3])))
        elif shape_name == 'Circle':
            shapes.append(Circle(int(shape[1])))

def find_max_area_and_perimeter(shapes):
    max_area = 0
    max_perimeter = 0
    max_area_shape = None
    max_perimeter_shape = None

    for shape in shapes:
        area = shape.area()
        perimeter = shape.perimeter()

        if area > max_area:
            max_area = area
            max_area_shape = shape

        if perimeter > max_perimeter:
            max_perimeter = perimeter
            max_perimeter_shape = shape

    return max_area_shape,max_area, max_perimeter_shape, max_perimeter


print(find_max_area_and_perimeter(shapes))
import math

square = float(input('What is the length of a side of the square in centimeters? '))
area_square_cm = square ** 2
area_square_m = area_square_cm / 10000
print(f'The area of the square is: {area_square_cm:.3f} cm^2')
print(f'The area of the square is: {area_square_m:.3f} m^2\n')

length = float(input('What is the length of rectangle in centimeters? '))
width = float(input('What is the width of the rectangle in centimeters? '))
area_rectangle = length * width
area_rectangle_m = area_rectangle / 10000
print(f'The area of the rectangle is: {area_rectangle:.3f} cm^2')
print(f'The area of the rectangle is: {area_rectangle_m:.3f} m^2\n')

radius = float(input('What is the radius of the circle in centimeters? '))
area_circle = math.pi * (radius ** 2)
area_circle_m = area_circle / 10000
print(f'The area of the circle is: {area_circle:.3f} cm^2')
print(f'The area of the circle is: {area_circle_m:.3f} m^2\n')

distance = float(input('What is the distance? \n'))
area_square = distance ** 2
area_circle = math.pi * (distance ** 2)
volume_cube = distance ** 3
volume_sphere = (4/3) * math.pi * distance ** 3
print(f'The area of the square is: {area_square:.3f}')
print(f'The area of the circle is: {area_circle:.3f}')
print(f'The volume of the cube is: {volume_cube:.3f}')
print(f'The volume of the sphere is: {volume_sphere:.3f}')


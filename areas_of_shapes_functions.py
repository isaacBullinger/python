import math

shape = ''
area = float()

def compute_area_rectangle(length, width):
    area_rectangle = length * width
    return area_rectangle

def compute_area_square(square):
    area_square = compute_area_rectangle(square, square)
    return area_square

def compute_area_circle(radius):
    area_circle = math.pi * (radius ** 2)
    return area_circle

def compute_area(shape, distance, default_distance=0):
    if shape == 'square':
        area = compute_area_square(distance)

    elif shape == 'circle':
        area = compute_area_circle(distance)
    
    elif shape == 'rectangle':
        area = compute_area_rectangle(distance, default_distance)

    return area

while shape != 'quit':

    shape = input('Which shape do you have (type quit to end)? ').lower()

    if shape == 'square':
        side = float(input('What is the length of a side? '))
        area = compute_area(shape, side)
        print(f'The area of the {shape} is: {area:.3f}\n')

    elif shape == 'rectangle':
        length = float(input('What is the length? '))
        width = float(input('What is the width? '))
        area = compute_area(shape, length, width)
        print(f'The area of the {shape} is: {area:.3f}\n')

    elif shape == 'circle':
        radius = float(input('What is the radius? '))
        area = compute_area(shape, radius)
        print(f'The area of the {shape} is: {area:.3f}\n')
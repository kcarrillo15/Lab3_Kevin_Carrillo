import math
from collections import Counter

def sphere_properties(radius):
    diameter = 2 * radius
    circumference = 2 * math.pi * radius
    surface_area = 4 * math.pi * radius ** 2
    volume = (4/3) * math.pi * radius ** 3
    return diameter, circumference, surface_area, volume

radius = float(input("Enter the radius of the sphere: "))

diameter, circumference, surface_area, volume = sphere_properties(radius)
print(f"Diameter: {diameter}")
print(f"Circumference: {circumference}")
print(f"Surface Area: {surface_area}")
print(f"Volume: {volume}")

def mean(numbers):
    return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2

def median(numbers):
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 0:
        
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        
        return sorted_numbers[mid]

def mode(numbers):
    
    count = Counter(numbers)
    max_frequency = max(count.values())
    mode_values = [num for num, freq in count.items() if freq == max_frequency]

    if len(mode_values) == 1:
        return mode_values[0]  
    else:
        return mode_values
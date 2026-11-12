import math


def calculate_volume(radius, height):
    """
    calculate and return the volume of the cylinder parameters:
        radius: the radius of the cylinder
        height: the height of the cylinder
    return: the volume of the cylinder
    """
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative.")

    volume = math.pi * (radius**2) * height
    return volume


def calculate_surface_area(radius, height):
    """
    calculate and return the surface area of the cylinder parameters:
        radius: the radius of the cylinder
        height: the height of the cylinder
    return: the surface area of the cylinder
    """
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative.")

    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

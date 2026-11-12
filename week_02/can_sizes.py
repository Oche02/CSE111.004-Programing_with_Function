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


def calculate_storage_efficiency(volume, surface_area):
    """
    calculate and return the storage efficiency of the cylinder parameters:
        volume: the volume of the cylinder
        surface_area: the surface area of the cylinder
    return: the storage efficiency of the cylinder
    """
    efficiency = volume / surface_area
    return efficiency


def main():
    # compute the volume of a can by calling input function.
    name = "#1 Picnic"
    radius = 6.83
    height = 10.16
    volume = calculate_volume(radius, height)

    # compute the surface area of a can by calling surface_area function.
    surface_area = calculate_surface_area(radius, height)

    # compute the storage efficiency of a can by calling storage_efficiency function.
    storage_efficiency = calculate_storage_efficiency(volume, surface_area)

    # print the storage efficiency of a can.
    print(f"{name}: {storage_efficiency:.2f}")

main()
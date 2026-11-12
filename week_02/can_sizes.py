import math

def compute_volume(radius, height):
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


def compute_surface_area(radius, height):
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


def compute_storage_efficiency(radius, height):
    """
    calculate and return the storage efficiency of the cylinder parameters:
        radius: the radius of the cylinder
        height: the height of the cylinder
    return: the storage efficiency of the cylinder
    """
    # compute the volume of a can.
    volume = compute_volume(radius, height)

    # compute the surface area of a can.
    surface_area = compute_surface_area(radius, height)

    # compute the storage efficiency of a can.
    storage_efficiency = volume / surface_area

    # return the storage efficiency of a can.
    return storage_efficiency

def compute_cost_efficiency(radius, height, cost_per_can):
    """
    calculate and return the cost efficiency of the cylinder parameters:
        radius: the radius of the cylinder
        height: the height of the cylinder
        cost_per_can: the cost of each can
    return: the cost efficiency of the cylinder
    """
    # compute the volume of a can.
    volume = compute_volume(radius, height)
    cost_efficiency = volume / cost_per_can
    return cost_efficiency


def main():
    # Four parallel lists, one list for each attribute of the cans.
    can_names = [
        "#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5",
        "#6Z", "#8Z short", "#10", "#211", "#300", "#303"
    ]
    can_radiuses = [
        6.83, 7.78, 8.73, 10.32, 10.79, 13.02,
        5.4, 6.83, 15.72, 6.83, 7.62, 8.1
    ]
    can_heights = [
        10.16, 11.91, 11.59, 11.91, 17.78, 14.29,
        8.89, 7.62, 17.78, 12.38, 11.27, 11.11
    ]
    can_costs = [
        0.28, 0.43, 0.45, 0.61, 0.86, 0.83,
        0.22, 0.26, 1.53, 0.34, 0.38, 0.42
    ]

    # For each can in the parallel lists, unpack the values
    # into the variables name, radius, height, and cost.
    for i in range(len(can_names)):
        name = can_names[i]
        radius = can_radiuses[i]
        height = can_heights[i]
        cost_per_can = can_costs[i]

        # compute the storage efficiency of a can by calling storage_efficiency function.
        storage_efficiency = compute_storage_efficiency(radius, height)

        # compute the cost efficiency of a can by calling cost_efficiency function.
        cost_efficiency = compute_cost_efficiency(radius, height, cost_per_can)

        # print the storage efficiency and cost efficiency of a can.
        print(f"{name}: {storage_efficiency:.2f} {cost_efficiency:.2f}")

main()
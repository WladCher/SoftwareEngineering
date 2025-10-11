import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

def triangle_area(x, y, z):
    half_p = (x + y + z) / 2
    return math.sqrt(max(0, half_p * (half_p - x) * (half_p - y) * (half_p - z)))

sides_max = (max(one), max(two), max(three))
sides_min = (min(one), min(two), min(three))

area_max = triangle_area(*sides_max)
area_min = triangle_area(*sides_min)

print("Стороны (max):", sides_max, "Площадь: ", area_max)
print("Стороны (min): ", sides_min, "Площадь:", area_min)

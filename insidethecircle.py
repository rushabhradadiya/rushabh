import math

def check_point_in_circle(x_center, y_center, radius, x, y):
    distance = math.sqrt((x - x_center)*2 + (y - y_center)*2)
    
    if distance < radius:
        return "Point lies inside the circle"
    elif distance == radius:
        return "Point lies on the circle"
    else:
        return "Point lies outside the circle"

x_center, y_center = map(int, input("Enter the center coordinates of the circle (x, y): ").split())
radius = float(input("Enter the radius of the circle: "))
x, y = map(int, input("Enter the point coordinates (x, y): ").split())
print(check_point_in_circle(x_center, y_center, radius, x, y))
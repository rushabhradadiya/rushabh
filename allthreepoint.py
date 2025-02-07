def check_collinearity(x1, y1, x2, y2, x3, y3):
    # Using the area of triangle formula to check collinearity
    area = (x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
    if area == 0:
        return "The points lie on one straight line"
    else:
        return "The points do not lie on one straight line"

x1, y1 = map(int, input("Enter the coordinates of point 1 (x1, y1): ").split())
x2, y2 = map(int, input("Enter the coordinates of point 2 (x2, y2): ").split())
x3, y3 = map(int, input("Enter the coordinates of point 3 (x3, y3): ").split())
print(check_collinearity(x1, y1, x2, y2, x3, y3))
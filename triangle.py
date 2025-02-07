def check_triangle_validity(a, b, c):
    if a + b + c == 180:
        return "Valid Triangle"
    else:
        return "Invalid Triangle"

a = int(input("Enter angle 1: "))
b = int(input("Enter angle 2: "))
c = int(input("Enter angle 3: "))
print(check_triangle_validity(a, b, c))
# 1. Add two numbers
a, b = map(int, input().split())
print(a + b)

# 2. Subtract two numbers
a, b = map(int, input().split())
print(a - b)

# 3. Multiply two numbers
a, b = map(int, input().split())
print(a * b)

# 4. Divide two numbers
a, b = map(int, input().split())
print(a / b)

# 5. Add, multiply, subtract, and divide two numbers
a, b = map(int, input().split())
print(a + b, a - b, a * b, a / b)

# 6. Convert hours into minutes
hours = int(input())
print(hours * 60)

# 7. Convert minutes into hours
minutes = int(input())
print(minutes / 60)

# 8. Convert dollars into Rs. (1$ = 48 Rs)
dollars = float(input())
print(dollars * 48)

# 9. Convert Rs. into dollars (1$ = 48 Rs)
rupees = float(input())
print(rupees / 48)

# 10. Convert dollars into pounds (1$ = 48 Rs, 1 pound = 70 Rs)
dollars = float(input())
print((dollars * 48) / 70)

# 11. Convert grams into kg
grams = float(input())
print(grams / 1000)

# 12. Convert kg into grams
kg = float(input())
print(kg * 1000)

# 13. Convert bytes into KB, MB, GB
bytes_value = int(input())
print(bytes_value / 1024, bytes_value / (1024*2), bytes_value / (1024*3))

# 14. Convert Celsius into Fahrenheit
celsius = float(input())
print((9/5) * celsius + 32)

# 15. Convert Fahrenheit into Celsius
fahrenheit = float(input())
print(5/9 * (fahrenheit - 32))

# 16. Calculate simple interest (I = PRN/100)
P, R, N = map(float, input().split())
print((P * R * N) / 100)

# 17. Calculate area & perimeter of a square
L = float(input())
print(L**2, 4 * L)

# 18. Calculate area & perimeter of a rectangle
L, B = map(float, input().split())
print(L * B, 2 * (L + B))

# 19. Calculate area of a circle (A = πR²)
R = float(input())
print((22/7) * R * R)

# 20. Calculate area of a triangle (A = ½ * b * h)
H, L = map(float, input().split())
print((H * L) / 2)

# 21. Calculate net salary
gross_salary = float(input())
allowance = gross_salary * 0.1
deduction = gross_salary * 0.03
net_salary = gross_salary + allowance - deduction
print(net_salary)

# 22. Calculate net sales
gross_sales = float(input())
net_sales = gross_sales - (gross_sales * 0.1)
print(net_sales)

# 23. Calculate the average of three subjects
s1, s2, s3 = map(float, input().split())
total = s1 + s2 + s3
print(total, total / 3)

# 24. Swap two values
a, b = map(int, input().split())
a, b = b, a
print(a, b)

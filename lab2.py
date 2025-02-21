# 1. Print largest and smallest values out of two
a, b = map(int, input().split())
print(max(a, b), min(a, b))

# 2. Print largest and smallest values out of three
a, b, c = map(int, input().split())
print(max(a, b, c), min(a, b, c))

# 3. Check whether a given number is odd or even
n = int(input())
print("Even" if n % 2 == 0 else "Odd")

# 4. Check whether a given number is divisible by 10 or not
n = int(input())
print("Divisible by 10" if n % 10 == 0 else "Not Divisible by 10")

# 5. Accept age of a person and determine if minor or major
age = int(input())
print("Minor" if age < 18 else "Major")

# 6. Accept a number and print the number of digits
n = input()
print(len(n))

# 7. Accept a year and check whether it is a leap year
year = int(input())
print("Leap Year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "Not a Leap Year")

# 8. Check if a triangle is valid based on its angles
a, b, c = map(int, input().split())
print("Valid Triangle" if a + b + c == 180 else "Invalid Triangle")

# 9. Print absolute value of a given number
n = int(input())
print(abs(n))

# 10. Check if area of rectangle is greater than perimeter
l, b = map(float, input().split())
print("Area is greater" if l * b > 2 * (l + b) else "Perimeter is greater")

# 11. Check if three points are collinear
x1, y1, x2, y2, x3, y3 = map(float, input().split())
print("Collinear" if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1) else "Not Collinear")

# 12. Determine position of a point relative to a circle
import math
x, y, r, px, py = map(float, input().split())
d = math.sqrt((px - x) * 2 + (py - y) * 2)
print("Inside Circle" if d < r else "On Circle" if d == r else "Outside Circle")

# 13. Convert numbers 0-19 to words
words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
         "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
         "Eighteen", "Nineteen"]
n = int(input())
print(words[n] if 0 <= n <= 19 else "Invalid Input")

# 14. Student result calculation with grading
s1, s2, s3 = map(int, input().split())
total = s1 + s2 + s3
average = total / 3
fail = s1 <= 39 or s2 <= 39 or s3 <= 39
grade = "NA" if min(s1, s2, s3) == 0 else \
        "F" if average <= 39 else \
        "P" if average <= 44 else \
        "C" if average <= 49 else \
        "B" if average <= 54 else \
        "B+" if average <= 59 else \
        "A" if average <= 69 else \
        "A+" if average <= 79 else "O"
print(total, average, "Fail" if fail else "Pass", grade)

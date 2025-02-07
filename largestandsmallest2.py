def find_largest_smallest(num1, num2):
    largest = max(num1, num2)
    smallest = min(num1, num2)
    return largest, smallest

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

largest, smallest = find_largest_smallest(num1, num2)

print("Largest value:", largest)
print("Smallest value:", smallest)
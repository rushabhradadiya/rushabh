# Input two values
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

# Display values before swapping
print("\nBefore swapping:")
print("a =", a)
print("b =", b)

# Swapping values
a, b = b, a

# Display values after swapping
print("\nAfter swapping:")
print("a =", a)
print("b =", b)
def count_digits(num):
    return len(str(abs(num)))  # abs to handle negative numbers as well

num = int(input("Enter a number: "))
print(f"The number of digits in the number is: {count_digits(num)}")
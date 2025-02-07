def check_divisible_by_10(num):
    if num % 10 == 0:
        return "Divisible by 10"
    else:
        return "Not divisible by 10"

num = int(input("Enter a number: "))
print(check_divisible_by_10(num))
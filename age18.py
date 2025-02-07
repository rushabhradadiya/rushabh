def check_age_category(age):
    if age < 18:
        return "Minor"
    else:
        return "Major"

age = int(input("Enter age: "))
print(check_age_category(age))
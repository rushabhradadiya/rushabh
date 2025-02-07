def number_to_word(num):
    words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    if 0 <= num <= 19:
        return words[num]
    else:
        return "Invalid number"

num = int(input("Enter a number between 0 and 19: "))
print(number_to_word(num))
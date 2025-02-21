# 1) Count number of boys and girls in a list
data = [("John", "Mike"), "Alice", ("David", "Steve"), "Emily"]
boys_count = sum(1 for item in data if isinstance(item, tuple))
girls_count = sum(1 for item in data if not isinstance(item, tuple))
print("1) Boys:", boys_count, "Girls:", girls_count)

# 2) Extract roll no, name, and age from tuple list
students = [(101, "Alice", 20), (102, "Bob", 21), (103, "Charlie", 22)]
roll_numbers = [x[0] for x in students]
names = [x[1] for x in students]
ages = [x[2] for x in students]
print("2) Roll Numbers:", roll_numbers)
print("2) Names:", names)
print("2) Ages:", ages)

# 3) Find difference between two date tuples
from datetime import date
date1 = (2024, 2, 10)
date2 = (2024, 3, 15)
d1 = date(*date1)
d2 = date(*date2)
days_difference = abs((d2 - d1).days)
print("3) Days between dates:", days_difference)

# 4) Sort a list of tuples by price in descending order
food_items = [("Burger", 50), ("Pizza", 100), ("Pasta", 80)]
sorted_food = sorted(food_items, key=lambda x: x[1], reverse=True)
print("4) Sorted Food Items:", sorted_food)

# 5) Remove empty tuples from a list
tuples_list = [(), (1, 2), (), (3, 4, 5), ()]
filtered_list = [t for t in tuples_list if t]
print("5) List after removing empty tuples:", filtered_list)

# 6) Modify an element of a tuple
tpl = (10, 20, 30, 40)
tpl = tpl[:2] + (99,) + tpl[3:]
print("6) Modified Tuple:", tpl)

# 7) Delete an element from a tuple
tpl = (1, 2, 3, 4, 5)
tpl = tpl[:2] + tpl[3:]
print("7) Tuple after deletion:", tpl)

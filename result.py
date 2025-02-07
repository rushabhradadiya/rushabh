def calculate_grades(marks):
    grades = []
    for mark in marks:
        if mark < 40:
            grades.append("F")
        elif mark <= 44:
            grades.append("P")
        elif mark <= 49:
            grades.append("C")
        elif mark <= 54:
            grades.append("B")
        elif mark <= 59:
            grades.append("B+")
        elif mark <= 69:
            grades.append("A")
        elif mark <= 79:
            grades.append("A+")
        else:
            grades.append("O")
    return grades

def check_pass_or_fail(marks):
    if any(mark < 40 for mark in marks):
        return "Fail"
    else:
        return "Pass"

marks = []
for i in range(1, 4):
    marks.append(int(input(f"Enter marks for subject {i}: ")))

total = sum(marks)
average = total / 3
grades = calculate_grades(marks)
status = check_pass_or_fail(marks)

print(f"Total marks: {total}, Average: {average}")
print(f"Pass/Fail: {status}")
print(f"Grades: {grades}")
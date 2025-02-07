gross_salary = float(input("Enter gross salary: "))
allowance = 0.1 * gross_salary
deduction = 0.03 * gross_salary
net_salary = gross_salary + allowance - deduction
print("Net Salary:", net_salary)
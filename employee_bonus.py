import csv

infile = open("EmployeePay.csv", "r")

employee_pay = csv.reader(infile, delimiter=",")
next(employee_pay)

for record in employee_pay:
    print("Fname:", record[1])
    print("Lname:", record[2])
    print("Salary: $" + str(record[3]))
    bonus = record[3] * record[4]
    print("Bonus: $" + str(bonus))
    total_pay = record[3] + bonus
    print("Total pay: $" + str(total_pay))
    input()

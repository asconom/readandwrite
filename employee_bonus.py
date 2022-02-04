import csv

infile = open("EmployeePay.csv", "r")

employee_pay = csv.reader(infile, delimiter=",")
next(employee_pay)

for record in employee_pay:
    print("Fname:", record[1])
    print("Lname:", record[2])
    print("Salary: $" + record[3])
    bonus = int(record[3]) * float(record[4])
    total_pay = int(record[3]) + (round(bonus, 2))
    print("Bonus: $" + str(round(bonus, 2)))

    print("Total pay: $" + str(total_pay))
    input()

infile.close()

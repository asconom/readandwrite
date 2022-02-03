from asyncore import write
import csv


customers = open("customers.csv", "r")
customer_country = open("customer_country.csv", "w")

customer_file = csv.reader(customers, delimiter=",")

count = -1
for record in customer_file:
    customer_country.write(record[1] + "," + record[2] + "," + record[4] + "\n")
    count += 1
print("Total number of customers:", count)

import csv

infile = open('Student_Scores.csv', 'r')
outfile = open('student_avg.csv', 'w')

score_file = csv.reader(infile, delimiter=',')
outfile.write('Name,Average\n')

for record in score_file:
    test_1 = int(record[1])
    test_2 = int(record[2])
    test_3 = int(record[3])
    average = (test_1 + test_2 + test_3) / 3
    outfile.write(record[0] + ',' + str(round(average, 2)) + '\n')

infile.close()
outfile.close()
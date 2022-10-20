import csv

f = open("C:/Users/abhch/Documents/Uni/Year 5 S2 (2022)/FIT3179/FIT3179_Visualisation2/joined_pop_energy.csv", 'r')
output = open("C:/Users/abhch/Documents/Uni/Year 5 S2 (2022)/FIT3179/FIT3179_Visualisation2/joined_pop_energy_2020.csv", 'w')
reader = csv.reader(f)

data = []
for row in reader:
    if row[2] != '2021':
        data.append(row)


for row in data:
    write_data = ''
    for col in row:
        write_data += col + ','
    write_data += '\n'
    output.write(write_data)
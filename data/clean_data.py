import csv

output = open('FIT3179_Visualisation2\Datasets\cleaned_sub_energy_source2021.csv', 'w')
datafile = open("FIT3179_Visualisation2\Datasets\primary-sub-energy-source.csv", 'r')
reader = csv.reader(datafile)
data = []


header = True
for row in reader:
    if header:
        data.append(row)
    if row[1] != '':
        if row[2] == '2021':
            data.append(row)
    header = False


for row in data:
    write_data = ''
    for col in row:
        write_data += col + ','
    write_data += '\n'
    output.write(write_data)

datafile.close()
output.close()
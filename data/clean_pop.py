import csv

output = open("C:/Users/abhch/Documents/Uni/Year 5 S2 (2022)/FIT3179/FIT3179_Visualisation2/Datasets/pop/pop_clean.csv", 'w')
datafile = open("C:/Users/abhch/Documents/Uni/Year 5 S2 (2022)/FIT3179/FIT3179_Visualisation2/Datasets/pop/pop_raw.csv", 'r')
reader = csv.reader(datafile)
data = []

output.write("Entity,Code,Year,Population\n")

rownum = 1
for row in reader:
    if rownum == 1:
        years = row
    else:
        write_data = f'{row[0]},{row[1]}'
        colnum = 0
        for col in row:
            if colnum > 2:
                output.write(f"{write_data},{years[colnum]},{row[colnum]}\n")
            colnum += 1
    rownum += 1


datafile.close()
output.close()
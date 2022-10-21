import csv

f = open("C:/Users/abhch/Documents/Uni/Year 5 S2 (2022)/FIT3179/FIT3179_Visualisation2/data/joined_pop_energy.csv",'r')
reader = csv.reader(f)
output = open("C:/Users/abhch/Documents/Uni/Year 5 S2 (2022)/FIT3179/FIT3179_Visualisation2/data/transpose_pop_energy.csv",'w')

rownum = 0
for row in reader:
    if rownum == 0:
        headers = row
        colnum = 0
        for col in row:
            if colnum in [0,1,2]:
                output.write(col+',')
            if colnum == 12:
                output.write(col+',Consumption,Source\n')
            colnum += 1
    else:
        colnum = 0
        for col in row:
            if colnum > 2 and colnum < 12:
                output.write(f'{row[0]},{row[1]},{row[2]},{row[12]},{row[colnum]},{headers[colnum]}\n')
            colnum += 1
    rownum += 1

f.close()
output.close()
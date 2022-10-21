import csv

f = open("C:/Users/abhch/Documents/Uni/Year 5 S2 (2022)/FIT3179/FIT3179_Visualisation2/data/joined_pop_energy.csv",'r')
reader = csv.reader(f)
output = open("C:/Users/abhch/Documents/Uni/Year 5 S2 (2022)/FIT3179/FIT3179_Visualisation2/data/countries.csv",'w')

countries = []
first = True
for row in reader:
    if first:
        countries.append(row[0])
        first = False
    elif row[0] != countries[-1]:
        countries.append(row[0])
    
for c in countries:
    output.write("\""+c+'\",')

f.close()
output.close()
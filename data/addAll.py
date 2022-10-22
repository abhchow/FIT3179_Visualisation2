import csv

output = open("C:/Users/abhch/Documents/Uni/Year 5 S2 (2022)/FIT3179/FIT3179_Visualisation2/data/pop_energy.csv",'w')
f = open("C:/Users/abhch/Documents/Uni/Year 5 S2 (2022)/FIT3179/FIT3179_Visualisation2/data/transpose_pop_energy.csv",'r')
reader = csv.reader(f)

sources = ["Wind", "Hydro", "Solar", "Nuclear", "Biofuels", "GeoBiomass", "Coal", "Oil", "Gas"]
totals = [0]*len(sources)

sourcenum = 0
rownum = 0
for row in reader:
    if rownum == 0:
        # headers = row
        cols = len(row)
        for i in range(cols-1):
            output.write(row[i]+',')
        output.write(row[i+1]+'\n')
    else:
        colnum = 0
        cols = len(row)
        for i in range(cols-1):
            output.write(row[i]+',')
        output.write(row[i+1]+'\n')
        
        sourcenum = (sourcenum+1)%len(sources)
    rownum += 1

f.close()
output.close()
import csv

output = open("C:/Users/abhch/Documents/Uni/Year 5 S2 (2022)/FIT3179/FIT3179_Visualisation2/Datasets/pop/joined_pop_energy.csv", 'w')
energy = open("C:/Users/abhch/Documents/Uni/Year 5 S2 (2022)/FIT3179/FIT3179_Visualisation2/Datasets/pop/cleaned_sub_energy_source.csv", 'r')
ereader = csv.reader(energy)


rownum = 0
for erow in ereader:
    if rownum == 0:
        for col in erow:
            if col != '':
                output.write(col+',')
        output.write('Population\n')
    else:
        pop = open("C:/Users/abhch/Documents/Uni/Year 5 S2 (2022)/FIT3179/FIT3179_Visualisation2/Datasets/pop/pop_clean.csv", 'r')
        preader = csv.reader(pop)
        ecode = erow[1]
        eyear = erow[2]
        for prow in preader:
            pcode = prow[1]
            pyear = prow[2]
            # if pyear != '2021':
            if pcode == ecode and pyear == eyear:
                popval = prow[3]
                for col in erow:
                    if col != '':
                        output.write(col+',')
                    else:
                        output.write('0,')
                    
                output.write(popval+'\n')
                pop.close()
                break    
        pop.close()

    rownum += 1



# pop.close()
energy.close()
output.close()
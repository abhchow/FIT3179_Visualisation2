import pandas as pd
import csv

# output = open("C:/Users/abhch/Documents/Uni/Year 5 S2 (2022)/FIT3179/FIT3179_Visualisation2/Datasets/pop/joined_pop_energy.csv", 'w')
# energy = pd.read_csv("C:/Users/abhch/Documents/Uni/Year 5 S2 (2022)/FIT3179/FIT3179_Visualisation2/Datasets/pop/cleaned_sub_energy_source.csv", 'r')
# pop = pd.read_csv("C:/Users/abhch/Documents/Uni/Year 5 S2 (2022)/FIT3179/FIT3179_Visualisation2/Datasets/pop/pop_clean.csv", 'r')

# # newboi = energy.merge(pop,'Code')
# energy["col"] = energy.Code.astype(str) + " " + energy.Year.astype(str)
# pop["col"] = pop.Code.astype(str) + " " + pop.Year.astype(str)

# e1 = energy.merge(pop, on='col')
# e1.to_csv("C:/Users/abhch/Documents/Uni/Year 5 S2 (2022)/FIT3179/FIT3179_Visualisation2/Datasets/pop/joined_pop_energy_pd.csv")

e = pd.read_csv("C:/Users/abhch/Documents/Uni/Year 5 S2 (2022)/FIT3179/FIT3179_Visualisation2/Datasets/pop/joined_pop_energy.csv")
# print(e.Population)
# print("\n\n\n")
print(e.Code)
print("\n\n\n")
print(e)
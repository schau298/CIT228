import csv
import matplotlib.pyplot as plt
import numpy as np 

STATE=[]
POPESTIMATE2010=[]
POPESTIMATE2019 = []



with open('term_project2/data/popChangeonlyUS.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header_row=next(csv_reader)

    for row in csv_reader:
        POPESTIMATE2010.append(row[7])
        POPESTIMATE2019.append(row[16])

plt.bar(POPESTIMATE2010, 309321666, color ='red', label="2010 Population") 
plt.bar(POPESTIMATE2019, 328239523, color="blue",  label="2019 Population")
  
plt.ylabel("Population per Million") 
plt.xlabel("2010 vs 2019") 
plt.title("Change in US Population from 2010-2019") 
plt.legend(loc="best")

plt.show() 
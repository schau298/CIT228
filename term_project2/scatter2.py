import csv
import matplotlib.pyplot as plt

STATE=[]
POPESTIMATE2019=[]

with open('term_project2/data/pop_change2010_2019.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header_row=next(csv_reader)

    for row in csv_reader:
        STATE.append(row[4])
        POPESTIMATE2019.append(int(row[16]))

plt.scatter (STATE, POPESTIMATE2019, marker='d', color = 'b', s = 100)
plt.xticks (fontsize="5.5", rotation = 75)
plt.xlabel ('States', fontsize="5")
plt.ylabel ('Population Count per Hundred Million', c="red")
plt.title('Population in 2019',  c="red")

plt.show()
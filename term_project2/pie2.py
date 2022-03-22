import csv
import matplotlib.pyplot as plt

with open('term_project2/data/pop_exclStates.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header_row=next(csv_reader)

    NAME, POPESTIMATE2019 = [] , [] 
    for row in csv_reader:
        NAME.append(row[4])
        POPESTIMATE2019.append(int(row[27]))

plt.pie(POPESTIMATE2019, labels = NAME, autopct = '%.2f%%')
plt.suptitle('The Population Battle Of 2019 ', fontsize=20)
plt.axis('equal')

plt.show()
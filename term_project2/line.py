import csv
import matplotlib.pyplot as plt
from datetime import datetime


with open('term_project2/data/pop_exclStates.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header_row=next(csv_reader)

    NAME, BIRTHS2010, BIRTHS2019 = [] , [] , []
    for row in csv_reader:
        NAME.append(row[4])
        BIRTHS2010.append(int(row[27]))
        BIRTHS2019.append(int(row[36]))

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(NAME, BIRTHS2010, c='green')

plt.suptitle('Births by Region in 2010',  c="g")
plt.xticks(fontsize="1", rotation = 75)
ax.set_xlabel ('', fontsize="6")
ax.set_ylabel("# of Births")
ax.tick_params(axis='both', which='major', labelsize=7)

plt.show()
  


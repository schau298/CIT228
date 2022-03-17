import matplotlib.pyplot as plt


labels = 'PNG', 'JPEG', 'SVG', 'GIF', 'Other'
used_at_sites = [376, 348, 153, 104, 19]
explode = (.25, 0, 0, 0, 0)  # only "explode" the 1st wedge
wedgeColors=('lightblue','lightyellow','lightpink','orange','lightgrey')

fig1, ax1 = plt.subplots()
ax1.pie(used_at_sites, explode=explode, labels=labels, autopct='%4.1f%%', shadow=True, startangle=20, colors=wedgeColors)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.suptitle("Popular Graphic Formats on the Web")

plt.show()
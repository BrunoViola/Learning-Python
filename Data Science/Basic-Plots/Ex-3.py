import matplotlib.pyplot as plt

year = [1950, 1951, 1952, 1960, 1970, 1980, 1990, 2000, 2015, 2020, 2024, 2100]
pop = [2.538, 2.57, 2.62, 3.03, 3.69, 4.44, 5.29, 6.14, 7.4, 7.82, 8.03, 10.85]

year = [1800, 1850, 1900] + year
pop = [1.0, 1.262, 1.650] + pop

plt.plot(year, pop)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks([0, 2, 4, 6, 8, 10],
           ['0', '2B', '4B', '6B', '8B', '10B'])
plt.show()
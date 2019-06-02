import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

years = [1950, 1955, 1960, 1965,
         1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]
pop = [2.5, 2.7, 3.0,
       3.3, 3.6, 4.0, 4.4, 4.8, 5.3, 5.7, 6.1, 6.5, 6.9, 7.3]

# plt.plot(years, pop, color=(255/255, 110/255, 110/255))

# plt.show()

lines = plt.plot(years, pop)

plt.setp(lines, color="blue", marker = "o")
plt.xlabel("Year")
plt.ylabel("Population")
plt.title ("World population line chart")
plt.show()
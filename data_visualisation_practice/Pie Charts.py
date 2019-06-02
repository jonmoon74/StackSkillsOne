import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


labels = 'Python', 'C++', 'Ruby', 'Java', 'Perl', 'R'
sizes = [62, 48, 52, 36, 21, 58]
separated = (0.2, 0, 0, 0, 0, 0)


plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=separated)
plt.axis('equal')
plt.show()

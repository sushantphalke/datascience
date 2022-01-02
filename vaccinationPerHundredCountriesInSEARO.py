import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
vaccinationfile = pd.read_csv('vaccination-data.csv')
Countries = []
vaccinationperhandred = []

for n in range(0, vaccinationfile.index[-1]):
    if (vaccinationfile['WHO_REGION'][n] == 'SEARO'):
        Countries.append(vaccinationfile['COUNTRY'][n])
        vaccinationperhandred.append(
            vaccinationfile['PERSONS_FULLY_VACCINATED_PER100'][n])

x = np.arange(len(Countries))  # the label locations
width = 0.7  # the width of the bars

fig, ax = plt.subplots(figsize=(11, 7))
rects2 = ax.bar(x, vaccinationperhandred, width,
                label='No. of Peoples Per 100')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('No. of Vaccinations')
ax.set_title('Vaccinations per 100 in SEARO')
ax.set_xticks(x)
ax.set_xlabel('Countries')
ax.set_xticklabels(Countries)
ax.legend()

ax.bar_label(rects2, padding=3)

fig.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
vaccinationfile = pd.read_csv('vaccination-data.csv')
totalvaccinationsum = 0
for l in range(0, 227):
    totalvaccinationsum += vaccinationfile['TOTAL_VACCINATIONS'][l]
print(totalvaccinationsum)
sumofafro = 0
for m in range(0, 227):
    if (vaccinationfile['WHO_REGION'][m] == 'AFRO'):
        sumofafro += vaccinationfile['TOTAL_VACCINATIONS'][m]

print(sumofafro)
sumofamro = 0
for n in range(0, 227):
    if (vaccinationfile['WHO_REGION'][n] == 'AMRO'):
        sumofamro += vaccinationfile['TOTAL_VACCINATIONS'][n]

print(sumofamro)
sumofemro = 0
sumofeuro = 0
sumofother = 0
sumofsearo = 0
sumofwpro = 0
for o in range(0, 227):
    if (vaccinationfile['WHO_REGION'][o] == 'EMRO'):
        sumofemro += vaccinationfile['TOTAL_VACCINATIONS'][o]
    if (vaccinationfile['WHO_REGION'][o] == 'EURO'):
        sumofeuro += vaccinationfile['TOTAL_VACCINATIONS'][o]
    if (vaccinationfile['WHO_REGION'][o] == 'OTHER'):
        sumofother += vaccinationfile['TOTAL_VACCINATIONS'][o]
    if (vaccinationfile['WHO_REGION'][o] == 'SEARO'):
        sumofsearo += vaccinationfile['TOTAL_VACCINATIONS'][o]
    if (vaccinationfile['WHO_REGION'][o] == 'WPRO'):
        sumofwpro += vaccinationfile['TOTAL_VACCINATIONS'][o]

print(sumofemro)
print(sumofeuro)
print(sumofother)
print(sumofsearo)
print(sumofwpro)
sumofafro+sumofamro+sumofemro+sumofeuro+sumofother+sumofsearo+sumofwpro


def calculaltePercentage(value1, totalvaccinationsum):
    percentage = ((value1 / totalvaccinationsum)*100)
    return percentage


afropercentage = calculaltePercentage(sumofafro, totalvaccinationsum)
amropercentage = calculaltePercentage(sumofamro, totalvaccinationsum)
emropercentage = calculaltePercentage(sumofemro, totalvaccinationsum)
europercentage = calculaltePercentage(sumofeuro, totalvaccinationsum)
otherpercentage = calculaltePercentage(sumofother, totalvaccinationsum)
searopercentage = calculaltePercentage(sumofsearo, totalvaccinationsum)
wpropercentage = calculaltePercentage(sumofwpro, totalvaccinationsum)
afropercentage+amropercentage+emropercentage+europercentage + \
    otherpercentage+searopercentage+wpropercentage
labels = 'AFRO', 'AMRO', 'EMRO', 'EURO', 'OTHER', 'SEARO', 'WPRO'
sizes = [afropercentage, amropercentage, emropercentage,
         europercentage, otherpercentage, searopercentage, wpropercentage]
explode = (0, 0, 0, 0, 0, 0.1, 0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.show()
arr = np.arange(1000000)

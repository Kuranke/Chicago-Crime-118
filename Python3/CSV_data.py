"""
Chicago-Crime-118 (PSIT Data Analysis Project)
CSV Script
"""

import csv
file = open('Chicago_Crimes_2005_to_2007.csv')
file2 = open('Chicago_Crimes_2001_to_2004.csv')
data = csv.reader(file)
data2 = csv.reader(file2)
table = [row for row in data]
table[:3]
table2 = [row for row in data2]
table[:3]
print(table)
print(table2)

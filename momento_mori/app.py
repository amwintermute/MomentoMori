import csv
from datetime import date

with open('data/life_expectancy.csv', mode='r') as life_expectancies:
    csv_reader = csv.DictReader(life_expectancies)
    line_count = 0
    data       = [row for row in csv_reader]

def years(gender, age):
    if gender == 'male':
        expectancy = data[age]['male life expectancy']
    else:
        expectancy = data[age]['male life expectancy']

    return float(expectancy)

def days(gender, age):
    return int(years(gender, age) * 365)

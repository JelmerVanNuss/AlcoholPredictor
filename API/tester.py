from requests import put, get
import csv

file = []
with open("D:\Downloads\YoungMavericksDownloads\data\clean_tac\BK7610_clean_TAC.csv", "r") as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        file += row
file = ','.join(file)
print(file)

#result = put('http://127.0.0.1:5000/data', data={'data': file})

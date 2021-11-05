from requests import put, get

with open("D:\Downloads\YoungMavericksDownloads\data\clean_tac\BK7610_clean_TAC.csv", "r") as f:
    file = f.read()

result = put('http://127.0.0.1:5000/data', data={'data': file})

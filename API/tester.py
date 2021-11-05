from requests import put, get

with open("D:\Downloads\YoungMavericksDownloads\data\clean_tac\BK7610_clean_TAC.csv", "r") as f:
    file = f.read()

#result = put('http://127.0.0.1:5000/data', data={'data': file})

#result = put('http://127.0.0.1:5000/predict', data={'data': file})
#print(get('http://127.0.0.1:5000/predict'))
# test_file = {
#     'Subject_ID': "35",
#     'IR Voltage': "1295",
#     'Temperature': "77903",
#     'Time': "10:45 PM",
#     'Date': "5-5-2017"
# }
test_file = {
    'delta_x': "3",
    'delta_y': "4",
    'delta_z': "5"
}

print(test_file)
print(put('http://127.0.0.1:5000/predict', data=test_file))


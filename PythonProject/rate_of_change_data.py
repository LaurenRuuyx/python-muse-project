import csv
import numpy as np


row_size = 300
w, h = row_size, 4
temp_2d_array = [[0 for x in range(w)] for y in range(h)]
global_2d_array = [[0 for x in range(40)] for y in range(10)]
# Iterate through the rows in the CSV file
iteration = 0
global_row = 0
with open('C:\\Users\\laurm\\Desktop\\ModelTesting\\test_data_1d - Copy.csv', 'r') as csvFile:
    # Create a reader object
    csv_reader = csv.reader(csvFile)
    for row in csv_reader:
        arr = []
        for i in range(0,40):
            lower = i * 30
            higher = (i+1) * 30
            value = int(((int(row[higher]) + 200) - (int(row[lower]) + 200))/30)
            # value = int(((int(row[higher])) - (int(row[lower])))/30)
            arr.append(value)
        # arr.append(row[len(row) - 1])
        global_2d_array[global_row] = arr
        global_row += 1
    print(global_2d_array)


with open('C:\\Users\\laurm\\Desktop\\ModelTesting\\changerates_test_data.csv', 'a',newline='') as csvfile:
    wr = csv.writer(csvfile) #, quoting=csv.QUOTE_ALL)
    wr.writerows(global_2d_array)


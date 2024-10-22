import csv
import numpy as np


row_size = 300
w, h = row_size, 4
temp_2d_array = [[0 for x in range(w)] for y in range(h)]
global_2d_array = [[0 for x in range(1201)] for y in range(10)]
# Iterate through the rows in the CSV file
iteration = 0
global_row = 0
with open('C:\\Users\\laurm\\Desktop\\ModelTesting\\test_data.csv', 'r') as csvFile:
    # Create a reader object
    csv_reader = csv.reader(csvFile)
    for row in csv_reader:
        temp_2d_array[iteration] = row
        iteration += 1
        if(iteration == 4):
            global_2d_array[global_row] = temp_2d_array[0] + temp_2d_array[1] + temp_2d_array[2] + temp_2d_array[3] + [row[0]]
            iteration = 0
            global_row += 1


        # if iteration != 4:
        #     temp_2d_array[iteration] = row
        #     iteration += 1
        # else:
        #     # if(row[0] == 4):
        #     #     row[0] = 0
        #     # global_2d_array[global_row] = temp_2d_array[0] + temp_2d_array[1] + temp_2d_array[2] + temp_2d_array[3] + [row[0]]
        #     # global_row += 1
        #     iteration = 0


with open('C:\\Users\\laurm\\Desktop\\ModelTesting\\test_data_1d.csv', 'a',newline='') as csvfile:
    wr = csv.writer(csvfile) #, quoting=csv.QUOTE_ALL)
    wr.writerows(global_2d_array)

import muselsl
import threading
from muselsl import muse, stream as stream_muse
from pylsl import StreamInlet, resolve_byprop
import time
import random
import csv

started = True
row_size = 300
w, h = row_size, 4
global_data_arr = [[0 for x in range(w)] for y in range(h)]
loop_count = 0
actions = ["nothing","up","down","left","right"]
csv_path = "C:\\Users\\laurm\\Desktop\\ModelTesting\\test_data.csv"

# Function that gets data from an EEG type stream. A stream needs to be started before the stream is looked up
def get_data_from_stream():
    # resolve_byprop will return an array with all found streams
    streams = resolve_byprop('type','EEG', timeout=20)
    # Check that a stream has been found
    # If not return early
    if len(streams) == 0:
        print("No EEG streams found, returning early")
        return
    inlet = StreamInlet(streams[0],max_chunklen=12,max_buflen=1)
    current_timestamp = time.time()
    while(started):
        inlet_tuple =  inlet.pull_sample(timeout=0.2)
        timestamp = inlet_tuple[1]
        if(current_timestamp > timestamp):
            continue
        data_array = inlet_tuple[0]
        print (data_array)
        counter = 0
        # for data in data_array:
        #     print(data)
            # global_data_arr[counter].append(data)
            # counter += 1
            
def process_and_clear_arr():
    for data in global_data_arr:
        print(data)

def record_data_from_stream():
    global global_data_arr
    global actions
    global row_size
    global loop_count
    recording_started = True
    # resolve_byprop will return an array with all found streams
    streams = resolve_byprop('type','EEG', timeout=20)
    # Check that a stream has been found
    # If not return early

    if len(streams) == 0:
        print("No EEG streams found, returning early")
        return
    
    inlet = StreamInlet(streams[0],max_chunklen=12,max_buflen=1)

    if inlet == None: return
    
    print("Starting data recording process")
    # random_integer = random.randint(0,4)
    random_integer = 4
    action = actions[random_integer]
    print("Please do the action " + action)
    input()
    rows = 0
    current_timestamp = time.time()
    print(current_timestamp)
    while(recording_started):
        inlet_tuple =  inlet.pull_sample(timeout=0.2)
        # print (inlet_tuple)
        data_array = inlet_tuple[0]
        try:
            if(current_timestamp > inlet_tuple[1]):
                continue
        except:
            print("Error Occurred")
            continue
        print(inlet_tuple)
        for i in range(4):
            # print(data_array[i])
            global_data_arr[i][rows] = data_array[i]
        rows = rows + 1
        # print(rows)
        # row_size is an arbitrarily selected number of how many data entries one row will have
        if (rows == row_size):
            print("reached limit for this sample.")
            print("Do you wish to save this sample for the action " + action + "? (Y/N)")
            save_input = input()

            if(save_input == "y"):
                print("saving this sample to csv")
                with open(csv_path,'a',newline='') as myfile:
                    wr = csv.writer(myfile) #, quoting=csv.QUOTE_ALL)
                    wr.writerows(global_data_arr)
                loop_count = loop_count + 1
            else:
                print("not saving this sample to csv")

            rows = 0
            global_data_arr = [[0 for x in range(w)] for y in range(h)]
            # random_integer = random.randint(0,4)
            random_integer = 4
            action = actions[random_integer]
            print(loop_count)
            print("Please do the action " + action)
            input()
            current_timestamp = time.time()
            print(current_timestamp)


    

record_data_from_stream()
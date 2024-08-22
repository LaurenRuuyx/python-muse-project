import muselsl
import threading
from muselsl import muse, stream as stream_muse
from pylsl import StreamInlet, resolve_byprop
import time
import random
import csv

started = True
w, h = 300, 4
global_data_arr = [[0 for x in range(w)] for y in range(h)]
actions = ["nothing","up","down","left","right"]
csv_path = "C:\\Users\\laurm\\Desktop\\data_recordings.csv"

# Function that gets data from an EEG type stream. A stream needs to be started before the stream is looked up
def get_data_from_stream():
    # resolve_byprop will return an array with all found streams
    streams = resolve_byprop('type','EEG', timeout=20)
    # Check that a stream has been found
    # If not return early
    if len(streams) == 0:
        print("No EEG streams found, returning early")
        return
    inlet = StreamInlet(streams[0],max_chunklen=12)
    while(started):
        inlet_tuple =  inlet.pull_sample(timeout=2)
        print (inlet_tuple)
        timestamp = inlet_tuple[1]
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
    recording_started = True
    # resolve_byprop will return an array with all found streams
    streams = resolve_byprop('type','EEG', timeout=20)
    # Check that a stream has been found
    # If not return early

    if len(streams) == 0:
        print("No EEG streams found, returning early")
        return
    
    inlet = StreamInlet(streams[0],max_chunklen=12)

    if inlet == None: return
    
    print("Starting data recording process")
    random_integer = random.randint(0,4)
    action = actions[random_integer]
    print("Please do the action " + action)
    input()
    rows = 0
    while(recording_started):
        inlet_tuple =  inlet.pull_sample(timeout=2)
        data_array = inlet_tuple[0]

        for i in range(4):
            # print(data_array[i])
            global_data_arr[i][rows] = data_array[i]
        rows = rows + 1
        print(rows)
        if (rows == 300):
            print("reached limit for this sample.")
            print("Do you wish to save this sample for the action " + action + "? (Y/N)")
            save_input = input()

            if(save_input == "y"):
                print("saving this sample to csv")
                with open(csv_path,'w',newline='') as myfile:
                    wr = csv.writer(myfile) #, quoting=csv.QUOTE_ALL)
                    wr.writerows(global_data_arr)
                    # wr.writerows(map(lambda x: [x], global_data_arr))
                    local_arr = [random_integer]
                    wr.writerow(local_arr)
                global_data_arr = [[0 for x in range(w)] for y in range(h)]

            else:
                print("not saving this sample to csv")
                global_data_arr = [[0 for x in range(w)] for y in range(h)]

            rows = 0
            random_integer = random.randint(0,4)
            action = actions[random_integer]
            print("Please do the action " + action)
            input()


    

record_data_from_stream()
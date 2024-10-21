import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib
import muselsl
import threading
from muselsl import muse, stream as stream_muse
from pylsl import StreamInlet, resolve_byprop
import time
import random
import csv


model = joblib.load("")
labels = ["nothing","up","down","left","right"]
row_size = 300
w, h = row_size, 4
global_data_arr = [[0 for x in range(w)] for y in range(h)]
loop_count = 0
csv_path = "C:\\Users\\laurm\\Desktop\\Fixed_data.csv"

def live_eeg_test():
    global global_data_arr
    global labels
    global row_size
    global loop_count

    started_loop = True
    streams = resolve_byprop('type','EEG', timeout=20)
    # Check that a stream has been found
    # If not return early

    if len(streams) == 0:
        print("No EEG streams found, returning early")
        return
    
    inlet = StreamInlet(streams[0],max_chunklen=12,max_buflen=1)

    if inlet == None: return
    
    rows = 0
    current_timestamp = time.time()

    while(started_loop):
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
            global_data_arr[i][rows] = int(data_array[i])
        rows = rows + 1

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
import numpy as np
from sklearn import preprocessing
from pynput.keyboard import Key,Controller
import tensorflow as tf
import keras




model = keras.models.load_model("C:\\Users\\laurm\\Documents\\GitHub\\python-muse-project\\Models\\Second_Model\\model.h5")
labels = ["nothing","up","down","left","right"]
row_size = 300
w, h = row_size, 4
global_data_arr = [[0 for x in range(w)] for y in range(h)]
loop_count = 0
# csv_path = "C:\\Users\\laurm\\Desktop\\Fixed_data.csv"
csv_path = "C:\\Users\\laurm\\Documents\\GitHub\\python-muse-project\\Models\\Second_Model\\deep_learning_FYP_model_4.pkl"


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
    print("Please do an action")
    input()
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
        if (rows == row_size):
            data = np.array(global_data_arr)
            min_max_scaler = preprocessing.MinMaxScaler()
            iter = 0
            element = min_max_scaler.fit_transform(data)
            predictarr = []
            predictarr.append(element)
            predictarr = np.array(predictarr)
            answer = model.predict(predictarr)
            answer = np.argmax(answer, axis=1)
            print(labels[answer[0]])
            rows = 0
            global_data_arr = [[0 for x in range(w)] for y in range(h)]
            print("Please do an action")
            input()
            current_timestamp = time.time()


live_eeg_test()
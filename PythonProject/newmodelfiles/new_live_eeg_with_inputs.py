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
from pynput.keyboard import Key,Controller
from playsound import playsound
import keras
import numpy as np
from sklearn import preprocessing


model = keras.models.load_model("C:\\Users\\laurm\\Documents\\GitHub\\python-muse-project\\Models\\Second_Model\\model.h5")
labels = ["nothing","up","down","left","right"]
row_size = 300
w, h = row_size, 4
global_data_arr = [[0 for x in range(w)] for y in range(h)]
global_1d_arr = []
keyboard = Controller()

def play_beep_noise():
    playsound(r'C:\\Users\laurm\Documents\GitHub\python-muse-project\PythonProject\beep.mp3')

def input_for_prediction(input_action):
    if(input_action == "nothing"):
        return
    if(input_action == "up"):
        keyboard.press('w')
        time.sleep(0.1)
        keyboard.release('w')
        return
    if(input_action == "down"):
        keyboard.press('s')
        time.sleep(0.1)
        keyboard.release('s')
        return
    if(input_action == "left"):
        keyboard.press('a')
        time.sleep(0.1)
        keyboard.release('a')
        return
    if(input_action == "right"):
        keyboard.press('d')
        time.sleep(0.1)
        keyboard.release('d')
        return

def live_eeg_test():
    global global_data_arr
    global labels
    global row_size
    global global_1d_arr

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
    play_beep_noise()
    current_timestamp = time.time()
    print("Please do an action")
    # input()
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
            predicted_action = labels[answer[0]]
            input_for_prediction(predicted_action)
            rows = 0
            global_data_arr = [[0 for x in range(w)] for y in range(h)]
            print("Please do an action")
            # input()
            play_beep_noise()
            current_timestamp = time.time()


live_eeg_test()
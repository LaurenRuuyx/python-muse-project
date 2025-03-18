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


model = joblib.load("C:\\Users\\laurm\\Desktop\\brainwave_model.pkl")
labels = ["nothing","up","down","left","right"]
row_size = 300
w, h = row_size, 4
global_data_arr = [[0 for x in range(w)] for y in range(h)]
global_1d_arr = []
changerates_arr = []
loop_count = 0
csv_path = "C:\\Users\\laurm\\Desktop\\Fixed_data.csv"
keyboard = Controller()

def play_beep_noise():
    playsound(r'C:\\Users\laurm\Documents\GitHub\python-muse-project\PythonProject\beep-06.mp3')

def input_for_prediction(input_action):
    if(input_action == "nothing"):
        return
    if(input_action == "up"):
        keyboard.press('w')
        time.sleep(0.1)
        keyboard.release('w')
        return
    if(input_action == "down"):
        keyboard.press(Key.down)
        time.sleep(0.1)
        keyboard.release(Key.down)
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
    global loop_count
    global global_1d_arr
    global changerates_arr

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
            global_1d_arr = global_data_arr[0] + global_data_arr[1] + global_data_arr[2] + global_data_arr[3]
            print(global_1d_arr)
            print(len(global_1d_arr))
            for j in range(0,40):
                lower = j * 30
                if(j == 39):
                    higher = ((j+1) * 30) - 1
                else:
                    higher = (j+1) * 30
                value = int(((int(global_1d_arr[higher]) + 200) - (int(global_1d_arr[lower]) + 200))/30)
                changerates_arr.append(value)
            # print(model.predict(changerates_arr))
            print(changerates_arr)
            print(len(changerates_arr))
            predictarr = []
            predictarr.append(changerates_arr)
            print(labels[model.predict(predictarr)[0]])
            predicted_action = labels[model.predict(predictarr)[0]]
            input_for_prediction(predicted_action)
            rows = 0
            global_data_arr = [[0 for x in range(w)] for y in range(h)]
            global_1d_arr = []
            changerates_arr = []
            # input()
            play_beep_noise()
            print("Please do an action")
            current_timestamp = time.time()


live_eeg_test()
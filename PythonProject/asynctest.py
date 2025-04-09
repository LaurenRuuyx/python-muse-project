import asyncio
from pynput.keyboard import Key,Controller
import time
import threading

keyboard = Controller()

def input_for_prediction(input_action):
    if(input_action == "nothing"):
        return
    if(input_action == "up"):
        keyboard.press(Key.up)
        time.sleep(1.5)
        keyboard.release(Key.up)
        return
    if(input_action == "down"):
        keyboard.press(Key.down)
        time.sleep(1.5)
        keyboard.release(Key.down)
        return
    if(input_action == "left"):
        keyboard.press(Key.left)
        time.sleep(1.5)
        keyboard.release(Key.left)
        return
    if(input_action == "right"):
        keyboard.press(Key.right)
        time.sleep(1.5)
        keyboard.release(Key.right)
        return
    
def main():
    threading.Thread(target=input_for_prediction, name="inputemulation", args=("up",)).start()
    time.sleep(1)
    threading.Thread(target=input_for_prediction, name="killer", args=("down",)).start()
    time.sleep(1)
    threading.Thread(target=input_for_prediction, name="killer", args=("left",)).start()
    time.sleep(1)
    threading.Thread(target=input_for_prediction, name="killer", args=("right",)).start()
    time.sleep(1)


main()
    

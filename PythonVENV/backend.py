from typing import Union

from fastapi import FastAPI

app = FastAPI()

player_1 = True


@app.get("/current_player")
def get_current_player():
    global player_1
    return player_1


@app.post("/current_player/swap")
def change_current_player():
    global player_1
    player_1 = not player_1
    return player_1

@app.post("/current_player/reset")
def reset_current_player():
    global player_1
    player_1 = True
    return player_1

import muselsl

import time

# Starts a stream with the first found muse device in the vicinity
# Needs to be run first, as a stream needs to be established before data is being sent to get_stream_data.py
# Need to look into multi-threading this function as it seems apparent to me that it will be helpful to code in multiple threads
def stream_thread_function():
    muses = muselsl.list_muses()
    # return early if no muses found
    if len(muses) == 0: return
    mac_address = muses[0]['address']
    # Start the lsl stream with the muse
    print(mac_address)
    muselsl.stream(mac_address)

stream_thread_function()
current_timestamp = time.time()
print(current_timestamp)
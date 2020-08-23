import os
import time
from datetime import datetime

from config import LOG_FILE, TIME_INTERVAL_SECONDS

process_id = 3
start_time = datetime.now()

while(True):
    # write to log file after every TIME_INTERVAL_SECONDS seconds
    if int(datetime.now().strftime('%S')) % TIME_INTERVAL_SECONDS == process_id - 1:
        # Open a file with access mode 'a'
        with open(LOG_FILE, "a") as file_object:
            # Append time_elapsed since script running at the end of file
            time_elapsed = (datetime.now() - start_time)
            file_object.write(os.path.basename(__file__) + ": Running since seconds " + str(time_elapsed.seconds))
            file_object.write("\n")
            time.sleep(TIME_INTERVAL_SECONDS)
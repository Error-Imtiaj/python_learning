##! DIGITAL TIME Project
from datetime import datetime
import time
import os




while(1):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    time.sleep(1)
    os.system("cls")
    time.sleep(0.00001)
    
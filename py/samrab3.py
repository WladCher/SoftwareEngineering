import time
from datetime import datetime

for i in range(5):
    print(datetime.now().strftime("%H:%M:%S"))
    time.sleep(1)                            
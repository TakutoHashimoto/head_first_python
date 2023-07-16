from datetime import datetime
import time
import random

odds = [x for x in range(1, 60) if x%2 != 0]

for _ in range(5):
    # right_this_minute = datetime.today().minute
    right_this_second = datetime.today().second

    if right_this_second in odds:
        print(f"{right_this_second}: 奇数")
    else:
        print(f"{right_this_second}: 奇数ではない")

    time.sleep(random.randint(1, 10))

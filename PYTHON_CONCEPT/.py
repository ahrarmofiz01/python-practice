import random
import time

while True:
    line = ''.join(random.choice("01") for _ in range(80))
    print(f"\033[92m{line}\033[0m")
    time.sleep(0. 05)

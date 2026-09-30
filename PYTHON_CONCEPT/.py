import math
import random
import time
import os

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

os.system("clear")

WIDTH = 80
HEIGHT = 25

phase = 0

while True:

    print("\033[H", end="")

    for y in range(HEIGHT):
        line = ""

        for x in range(WIDTH):

            wave = math.sin(
                x * 0.25 +
                y * 0.45 +
                phase
            )

            noise = random.random()

            if wave > 0.65 and noise > 0.45:
                char = random.choice("01{}[]<>/\\#$%@")
                line += GREEN + char + RESET

            elif wave < -0.75 and noise > 0.7:
                char = random.choice("01ABCDEF")
                line += RED + char + RESET

            else:
                line += " "

        print(line)

    phase += 0.15
    time.sleep(0.03)

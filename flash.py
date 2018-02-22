import os
import sys

long_x = os.get_terminal_size().columns
long_y = os.get_terminal_size().lines

while True:
    for i in range(0, long_x * long_y):
        sys.stdout.write("\033[0m#")
        i = i + 1
    i = 0
    for i in range(0,long_x*long_y):
        sys.stdout.write("\033[1;31;40m#")
        i = i + 1
    i = 0
import sys
import time

def clear_screen():
    print("\033[H", end="")

def render_frame(ascii_str):
    clear_screen()
    print(ascii_str)
    sys.stdout.flush()

print("\033[2J\033[H\033[?25l", end="")

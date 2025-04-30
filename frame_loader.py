import os
from concurrent.futures import ProcessPoolExecutor
from PIL import Image
import shutil

def get_terminal_size():
    size = shutil.get_terminal_size(fallback=(80, 24))
    return size.columns, size.lines

def image_to_ascii(path, width=640):
    cols, rows = get_terminal_size()

    # Leave a bit of padding for margins
    width = cols
    height = rows - 2
    img = Image.open(path).convert("L")
    img = img.resize((width, int(height)))
    pixels = img.getdata()

    chars = [' ', "#"]
    threshold = 128
    ascii_str = ''.join(chars[pixel > threshold] for pixel in pixels)

    ascii_lines = [ascii_str[i:i+img.width] for i in range(0, len(ascii_str), img.width)]
    return '\n'.join(ascii_lines)

def load_single_frame(path):
    return image_to_ascii(path)

def load_frames(frame_dir, max_workers=None):
    frame_files = sorted([os.path.join(frame_dir, f) for f in os.listdir(frame_dir) if f.endswith(".png") ])

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        frames = list(executor.map(load_single_frame, frame_files))

    return frames

import subprocess

def extract_frames():
    subprocess.run(["ffmpeg", "-i", "./【東方】Bad Apple!! ＰＶ【影絵】 [FtutLA63Cp8].mp4", "-vf", "fps=30", "./frames/frames%04d.png"])

def extract_audio():
    subprocess.run(["ffmpeg", "-i", "./【東方】Bad Apple!! ＰＶ【影絵】 [FtutLA63Cp8].mp4", "-vn", "-acodec", "pcm_s16le", "-ar", "44100", '-ac', '2', "bad_apple_audio.wav"])


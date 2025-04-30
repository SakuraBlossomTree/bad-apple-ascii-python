import time
import os
import subprocess
import video_extractor
import frame_extractor
import frame_loader
import frame_loader_60_fps
import frame_render
# import simpleaudio as sa
# from pydub import AudioSegment
import subprocess
import wave

BAD_APPLE_URL = "https://www.youtube.com/watch?v=FtutLA63Cp8"

frame_dir = "./frames/"

audio_path = "bad_apple_audio.wav"

print("Video extracting")

video_extractor.extract_video(BAD_APPLE_URL)

frame_extractor.extract_audio()

if not any(f.endswith(".png") for f in os.listdir(frame_dir)):
    frame_extractor.extract_frames()
#
frames = frame_loader.load_frames(frame_dir)

# for frame in frames:
#     frame_render.render_frame(frame)

def sync_frames_with_audio(frames, audio_path):
   
    with wave.open(audio_path, 'rb') as wf:
        frames_in_audio = wf.getnframes()
        framerate = wf.getframerate()
        audio_length = frames_in_audio / framerate

    # Start ffplay in background
    subprocess.Popen(['play', audio_path],
                     stdout=subprocess.DEVNULL,
                     stderr=subprocess.DEVNULL)

    frame_count = len(frames)
    frame_duration = audio_length / frame_count

    start_time = time.time()
    for i, frame in enumerate(frames):
        target_time = start_time + i * frame_duration 
        now = time.time()

        time_to_sleep = target_time - now
        if time_to_sleep > 0:
            time.sleep(time_to_sleep)

        frame_render.render_frame(frame)

    play_obj.wait_done()

sync_frames_with_audio(frames, audio_path)

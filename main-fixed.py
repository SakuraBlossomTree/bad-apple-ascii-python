import time
import os
import video_extractor
import frame_extractor
import frame_loader
import frame_render

BAD_APPLE_URL = "https://www.youtube.com/watch?v=FtutLA63Cp8"
frame_dir = "./frames/"

if __name__ == "__main__":
    print("Video extracting")

    video_extractor.extract_video(BAD_APPLE_URL)
    # frame_extractor.extract_audio()

    if not any(f.endswith(".png") for f in os.listdir(frame_dir)):
        frame_extractor.extract_frames()

    frames = frame_loader.load_frames(frame_dir)

    FPS = 30
    frame_duration = 1 / FPS

    for frame in frames:
        start_time = time.time()

        frame_render.render_frame(frame)

        elapsed = time.time() - start_time
        time_to_sleep = frame_duration - elapsed
        if time_to_sleep > 0:
            time.sleep(time_to_sleep)
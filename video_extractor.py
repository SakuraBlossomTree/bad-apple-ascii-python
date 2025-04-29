from yt_dlp import YoutubeDL

ydl_opts = {
            
            'format':"mp4/bestaudio/best",
            'noplaylist' : True,
            'quiet': True,
            'extract_flat': True,
            'verbose': True,
}

def extract_video(url):
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        return info_dict

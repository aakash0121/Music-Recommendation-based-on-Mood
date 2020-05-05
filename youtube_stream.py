import webbrowser
import yt_url

def play_video(input_str):
    webbrowser.open(yt_url.url(input_str))
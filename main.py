from pytube import YouTube

URL = 'https://www.youtube.com/watch?v=N9SG72poHJc'


yt = YouTube(URL)

print(f'Your Video title is {yt.title}')

print(f'and it had got {yt.views} views')
yt.streams.filter(progressive=True, file_extension='mp4').order_by(
    'resolution').desc().first().download()

# yt.register_on_progress_callback()
# yt.streams.filter(only_audio=True).all()

# yt.captions.get_by_language_code('en')

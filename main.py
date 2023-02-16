# Biblioteca Usada
from pytube import YouTube

# Variavel da url
VIDEO_URL = input(f'Digite a url do video: ')
yt = YouTube(VIDEO_URL)

# Fazer download do Video Melhor Qualidade
video = yt.streams.get_highest_resolution()

# Pasta desejada
video.download(output_path='Videos')
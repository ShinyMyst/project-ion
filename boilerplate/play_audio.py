import pygame

def play_audio_file(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


# Specify the path to your MP3 file
mp3_file = 'output.mp3'

# Play the MP3 file
play_audio_file(mp3_file)

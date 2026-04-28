import pygame

playlist = ["button-click-short-ringing-close-dry.wav", "button-click-clear-soft.wav"]
current = 0

def play():
    pygame.mixer.music.load(playlist[current])
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def next_track():
    global current
    current = (current + 1) % len(playlist)
    play()

def prev_track():
    global current
    current = (current - 1) % len(playlist)
    play()
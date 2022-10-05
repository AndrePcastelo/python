# esse exercício serve para colocar um audio mp3 no programa
import pygame
music = input('Cole o url da musica aqui por favor:')
pygame.mixer.init()
pygame.mixer.music.load(music)
pygame.mixer.music.play()
input()
pygame.event.wait()
#finalmente 
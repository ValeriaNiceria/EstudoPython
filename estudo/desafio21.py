'''
Faça um programa em python que abra e reproduza
o áudio de um programa MP3.
'''

import pygame
pygame.init()

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
pygame.event.wait()

# Fazer um programa que leia um arquivo MP3.

import pygame
import time

pygame.init()
pygame.mixer.music.load('../Gusttavo Lima.mp3')
pygame.mixer.music.play()

time.sleep(400)



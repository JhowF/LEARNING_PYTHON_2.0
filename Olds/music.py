import pygame
import time
print('Olá'.upper())
time.sleep(1)
print('Temos 3 opções de musicas no Neefex,\npodendo escolher essas musicas pelo seus números:'.upper())
time.sleep(3)
M=input('Diga me um número de 1 a 3 e tocarei uma das 3 musicas do Neffex: '.upper())
if M [0] == str(1):
    pygame.init()
    pygame.mixer.music.load('Greatful.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
    
    
    
    
    
    
    
elif M [0] == str(2):
    pygame.init()
    pygame.mixer.music.load('Cold.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
else :
    pygame.init()
    pygame.mixer.music.load('Careless.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
#pygame.init()
#pygame.mixer.music.load('Neefex.mp3')
#pygame.mixer.music.play()
#input()
#pygame.event.wait()


















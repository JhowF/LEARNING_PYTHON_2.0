import time

import pygame
name = 'Jonathan rodrigo ferreira dos santos'
print (name)

time.sleep(4)
amount = len (name)
print (f'O nome {name} ocupa {amount} espaços.  ')
print ('Existe a palavra santos?', 'santos' in name)
print ('Existe a Palavra Santos?', 'Santos' in name)

time.sleep(4)
print(name.replace('rodrigo','roque'))
print(name.replace('rodrigo',''))

time.sleep(3)
print (name.find('dos'))
print (name.strip())


time.sleep(3)
print (name [0:8], 'É para mostrar Jonathan')

time.sleep(4)
print (name.upper())
print (name.capitalize())
print(name.title())
print(name.lower())


time.sleep(5)
print('you can chose one of theses song, Careless, Cold or Greatful ')
time.sleep(3)
Song = input('Tell me, what song would you like to ear? ').upper()

if Song [0:3] == str('CAR'):
    pygame.init()
    pygame.mixer.music.load('Careless.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
elif Song [0:3] == 'COL':
    pygame.init()
    pygame.mixer.music.load('Cold.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
elif Song [0:3] == 'GRE':
    pygame.init()
    pygame.mixer.music.load('Greatful.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()

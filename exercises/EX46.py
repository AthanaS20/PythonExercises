import pygame
import time
print('=*' * 18)
print('CONTAGEM REGRESSIVA PARA O ANO NOVO')
print('=*' * 18)

for ano in range(10, -1, -1):
    time_duration = 1
    time.sleep(time_duration)
    print(ano)
print('FELIZ 2023!!')
pygame.init()
pygame.mixer.music.load('/home/athana/Documentos/GitHub/PythonExercises/exercises/queima.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

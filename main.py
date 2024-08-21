from classes.character import Character


character_instance = Character()


# print a charecter
print(character_instance.name)
print(character_instance.race)
print(character_instance.type)
print(character_instance.health)
print(character_instance.attack)
print(character_instance.defense)


import pygame
from pygame.locals import*

pygame.init()

window_width = 800
window_height = 600

window = pygame.display.set_mode((window_width, window_height))

character_image = pygame.image.load('images/sword001.png')

character_positon = [50, 50]

# GAMELOOP
running = True
while running:
    window.fill((255, 255, 255))

    window.blit(character_image, character_positon)

    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        
pygame.quit()

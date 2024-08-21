from classes.character import Character


character_instance = Character()

import pygame
from pygame.locals import*

pygame.init()

font = pygame.font.Font(None, 36)

window_width = 800
window_height = 600

window = pygame.display.set_mode((window_width, window_height))

character_image = pygame.image.load('images/sword001.png')

new_width = 25
new_height = 100
character_image = pygame.transform.scale(character_image, (new_width, new_height))

character_positon = [200, 50]


def display_text(text, position):
    surface = font.render(text, True, (255, 255, 255))
    window.blit(surface, position)


# GAMELOOP
running = True
while running:
    window.fill((0, 0, 0))

    window.blit(character_image, character_positon)

    display_text(character_instance.name, (10, 10))
    display_text(character_instance.race, (10, 50))
    display_text(character_instance.type, (10, 90))
    display_text(str(character_instance.health), (10, 130))
    display_text(str(character_instance.attack), (10, 170))
    display_text(str(character_instance.defense), (10, 210))

    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        
pygame.quit()

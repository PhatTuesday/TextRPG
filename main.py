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


# Utility Functions
def display_text(text, position):
    surface = font.render(text, True, (255, 255, 255))
    window.blit(surface, position)


def initial_game_screen():
    button_color = (0, 255, 0)
    button_position = (window_width // 2 - 50, window_height // 2 - 25)
    button_size = (100, 50)

# GAMELOOP
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if (button_position[0] <= mouse_position[0] <= button_position[0] + button_size[0] and
                        button_position[1] <= mouse_position[1] <= button_position[1] + button_size[1]):
                    character_screen()
                    running = False

        window.fill((0, 0, 0))
        pygame.draw.rect(window, button_color, pygame.Rect(button_position, button_size))


def character_screen():
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


initial_game_screen()

pygame.quit()

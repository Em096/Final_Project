import pygame

def main():
    pygame.init()
    pygame.display.set_caption("To Catch a Star")
    display_size = (500, 800)
    screen = pygame.display.set_mode(display_size)
    running = True
    while running:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # TODO: game logic
        # render & display
    pygame.quit()

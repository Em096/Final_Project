import pygame


def main():
    pygame.init()
    pygame.display.set_caption("To Catch a Star")
    clock = pygame.time.Clock()
    dt = 0
    display_size = (800, 500)
    screen = pygame.display.set_mode(display_size)
    bg = pygame.image.load('ToCatchAStar_BG.png')
    running = True
    while running:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # TODO: game logic
        # render & display
        screen.blit(bg, (0,0))
        pygame.display.flip()
        dt = clock.tick(12)
    pygame.quit()


class Star(pygame.sprite.Sprite):

if __name__ == "__main__":
    main()
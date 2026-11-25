import pygame


def main():
    pygame.init()
    pygame.display.set_caption("To Catch a Star")
    clock = pygame.time.Clock()
    dt = 0
    display_size = (800, 500)
    screen = pygame.display.set_mode(display_size)
    bg = pygame.image.load('ToCatchAStar_BG.png')
    star_grp = pygame.sprite.Group()
    star = Star(100, 250)
    star_grp.add(star)
    running = True
    while running:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # TODO: game logic
        # render & display
        screen.blit(bg, (0,0))
        star_grp.draw(screen)
        pygame.display.flip()
        dt = clock.tick(12)
    pygame.quit()


class Star(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('ToCatchAStar_Star.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

if __name__ == "__main__":
    main()
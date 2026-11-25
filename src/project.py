import random
import pygame


def main():
    pygame.init()
    pygame.display.set_caption("To Catch a Star")
    clock = pygame.time.Clock()
    dt = 0
    asteroid_duration = 1500
    time_since_last_ast = pygame.time.get_ticks()
    display_size = (800, 500)
    screen = pygame.display.set_mode(display_size)
    bg = pygame.image.load('ToCatchAStar_BG.png')
    star_grp = pygame.sprite.Group()
    star = Star(100, 250)
    star_grp.add(star)
    stardust_grp = pygame.sprite.Group()
    asteroid_grp = pygame.sprite.Group()
    running = True
    while running:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.sprite.groupcollide(star_grp, asteroid_grp, True, False):
                running = False
        
        time_elapsed = pygame.time.get_ticks()
        if time_elapsed - time_since_last_ast > asteroid_duration:
            asteroid = Asteroid(800, random.randrange(0, 500, 120))
            asteroid_grp.add(asteroid)
            time_since_last_ast = time_elapsed
        # TODO: game logic
        star.update()
        asteroid_grp.update()
        print(asteroid_grp)
        # render & display
        screen.blit(bg, (0,0))
        star_grp.draw(screen)
        asteroid_grp.draw(screen)
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

    def update(self):
        self.movement()
        self.rect.x += self.dx
        self.rect.y += self.dy

    def movement(self):
        self.dx = 0
        self.dy = 0
        player_speed = 10
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.dx -= player_speed
        if keys[pygame.K_RIGHT]:
            self.dx += player_speed
        if keys[pygame.K_DOWN]:
            self.dy += player_speed
        if keys[pygame.K_UP]:
            self.dy -= player_speed


class Stardust(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('ToCatchAStar_StarDust.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.movement()
        if self.rect.right < 0:
            self.kill()
            
    def movement(self):
        self.dust_speed = 15
        self.rect.x -= self.dust_speed
        

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('ToCatchAStar_Asteroid.png')
        self.rect = self.image.get_rect()
        self.ast_grp = pygame.sprite.Group()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.movement()
        if self.rect.right < 0:
            self.kill()
        
    def movement(self):
        self.ast_speed = 15
        self.rect.x -= self.ast_speed


if __name__ == "__main__":
    main()
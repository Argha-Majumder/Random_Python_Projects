# This is a simple game demo. The source code of this
# game was taken from the opensource.com

import pygame
import sys
import os

# Variables
worldx = 960
worldy = 600

fps = 40  # Frame rate
ani = 4  # Animation cycle

main = True

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)

# Objects
class Player(pygame.sprite.Sprite):

    # Spawn a player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1,5):
            img = pygame.image.load(os.path.join('venv\images\Sprites', 'hero-' + str(i) + '.png')).convert()
            img.convert_alpha()            # Optimise alpha
            img.set_colorkey(ALPHA)        # Set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()


# Setup
clock = pygame.time.Clock()
pygame.init()

world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load(os.path.join('venv\images\Backgrounds', 'backgroundForest.png'))
backdropbox = world.get_rect()

player = Player()    # Spawn player
player.rect.x = 0    # go to x
player.rect.y = 0    # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
# Main loop
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left')

            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right')

            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left stop')

            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right stop')

            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

    world.blit(backdrop, backdropbox)
    player_list.draw(world)   # Draw player
    pygame.display.flip()
    clock.tick(fps)

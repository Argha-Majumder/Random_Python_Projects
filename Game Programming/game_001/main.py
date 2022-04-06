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
        self.movex = 0   # move along x
        self.movey = 0   # move along y
        self.frame = 0   # count frames
        self.health = 0  # health
        self.images = []
        for i in range(1, 5):
            img = pygame.image.load(os.path.join('venv\images\Sprites', 'hero-' + str(i) + '.png')).convert()
            img.convert_alpha()  # Optimise alpha
            img.set_colorkey(ALPHA)  # Set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    # control player movement
    def control(self, x, y):
        self.movex += x
        self.movey += y

    # update sprite position
    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame // ani]

        hit_list = pygame.sprite.spritecollide(self,enemy_list,False)
        for enemy in hit_list:
            self.health -= 1
            print(self.health)


class Enemy(pygame.sprite.Sprite):
    """
    Spawn an enemy
    """

    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('venv\images\Sprites', 'enemy.png'))
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0  # counter variable

    def move(self):
        """
        Enemy movement
        """
        distance = 80
        speed = 8
        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
        elif self.counter >= distance and self.counter <= distance *2:
            self.rect.x -= speed
        else:
            self.counter = 0
        self.counter += 1

class Level():
    def bad(lvl,eloc):
        if lvl == 1:
            enemy = Enemy(eloc[0], eloc[1], 'venv\images\Sprites\enemy.png')    # spawn enemy
            enemy_list = pygame.sprite.Group()                                  # create enemy group
            enemy_list.add(enemy)                                               # add enemy to group

        if lvl == 2:
            print("Level "+str(lvl))
        return enemy_list

# Setup
clock = pygame.time.Clock()
pygame.init()

world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load(os.path.join('venv\images\Backgrounds', 'backgroundForest.png'))
backdropbox = world.get_rect()

player = Player()  # Spawn player
player.rect.x = 0  # go to x
player.rect.y = 0  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10  # how many pixels to move
# enemy = Enemy(300, 0, 'venv\images\Sprites\enemy.png')  # spawn enemy
# enemy_list = pygame.sprite.Group()  # create enemy group
# enemy_list.add(enemy)  # add enemy to group
eloc = []
eloc = [300,0]
enemy_list = Level.bad(1, eloc)

# Main loop
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps, 0)

            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps, 0)

            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)

            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps, 0)

            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False
    player.update()  # update player position
    world.blit(backdrop, backdropbox)
    player_list.draw(world)  # Draw player
    enemy_list.draw(world)  # refresh enemy
    for e in enemy_list:
        e.move()
    pygame.display.flip()
    clock.tick(fps)

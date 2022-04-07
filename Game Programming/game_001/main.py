# This is a simple game demo. The source code of this
# game was taken from the opensource.com

import pygame
import sys
import os

'''
Variables
'''

worldx = 1000
worldy = 600
forwardx = 600
backwardx = 230
fps = 40  # Frame rate
ani = 4  # Animation cycle

main = True

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)

'''
Objects
'''

class Player(pygame.sprite.Sprite):

    # Spawn a player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0    # move along x
        self.movey = 0    # move along y
        self.frame = 0    # count frames
        self.health = 10  # health
        self.is_jumping = True
        self.is_falling = False
        self.images = []
        for i in range(1, 5):
            img = pygame.image.load(os.path.join('venv\images\Sprites', 'hero-' + str(i) + '.png')).convert()
            img.convert_alpha()       # Optimise alpha
            img.set_colorkey(ALPHA)   # Set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    # control player movement
    def control(self, x, y):
        self.movex += x
        self.movey += y

    # control jump
    def jump(self):
        if self.is_jumping is False:
            self.is_falling = False
            self.is_jumping = True

    # update sprite position
    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # moving left
        if self.movex < 0:
            self.is_jumping = True
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

        # moving right
        if self.movex > 0:
            self.is_jumping = True
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame // ani]

        hit_list = pygame.sprite.spritecollide(self, enemy_list, False)
        for enemy in hit_list:
            self.health -= 1
            print(self.health)

        ground_hit_list = pygame.sprite.spritecollide(self, ground_list, False)
        for g in ground_hit_list:
            self.movey = 0
            self.rect.bottom = g.rect.top
            self.is_jumping = False       # stop jumping

        # fall of the world
        if self.rect.y > worldy:
            self.health -= 1
            print(self.health)
            self.rect.x = tx
            self.rect.y = ty

        if self.is_jumping and self.is_falling is False:
            self.is_falling = True
            self.movey -= 33          # how high to jump

        plat_hit_list = pygame.sprite.spritecollide(self, plat_list, False)
        for p in plat_hit_list:
            self.is_jumping = False   # stop jumping
            self.movey = 0

            # approach from below
            if self.rect.bottom <= p.rect.bottom:
                self.rect.bottom = p.rect.top
            else:
                self.movey += 3.2
    # simulating gravity
    def gravity(self):
        if self.is_jumping:
            self.movey += 3.2    # how fast player falls

        # if self.rect.y > worldy and self.movey >= 0:
        #     self.movey = 0
        #     self.rect.y = worldy-ty-ty

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
        elif self.counter >= distance and self.counter <= distance * 2:
            self.rect.x -= speed
        else:
            self.counter = 0
        self.counter += 1


class Level():
    def bad(lvl, eloc):
        if lvl == 1:
            enemy = Enemy(eloc[0], eloc[1], 'venv\images\Sprites\enemy.png')  # spawn enemy
            enemy_list = pygame.sprite.Group()  # create enemy group
            enemy_list.add(enemy)  # add enemy to group

        if lvl == 2:
            print("Level " + str(lvl))
        return enemy_list

    def ground(lvl, gloc, tx, ty):
        ground_list = pygame.sprite.Group()
        i = 0
        if lvl == 1:
            while i < len(gloc):
                ground = Platform(gloc[i], worldy-ty, tx, ty, 'venv\images\Sprites\ground.png')
                ground_list.add(ground)
                i = i + 1

        if lvl == 2:
            print("Level " + str(lvl))
        return ground_list

    def platform(lvl, tx, ty):
        plat_list = pygame.sprite.Group()
        ploc = []
        i = 0
        if lvl == 1:
            ploc.append((200, worldy-ty-128, 3))
            ploc.append((300, worldy-ty-256, 3))
            ploc.append((500, worldy-ty-128, 4))
            while i < len(ploc):
                j = 0
                while j <= ploc[i][2]:
                    plat = Platform((ploc[i][0]+(j*tx)), ploc[i][1], tx, ty, 'venv\images\Sprites\\block-big.png')
                    plat_list.add(plat)
                    j = j + 1
                print('run'+str(i)+str(ploc[i]))
                i = i + 1
        if lvl == 2:
            print("Level " + str(lvl))
        return plat_list


# x location, y location, img width, img height, img file
class Platform(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('venv\images\Sprites', 'ground.png')).convert()
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc


# Setup
clock = pygame.time.Clock()
pygame.init()

world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load(os.path.join('venv\images\Backgrounds', 'backgroundForest.png'))
backdropbox = world.get_rect()

player = Player()  # Spawn player
player.rect.x = 0   # go to x
player.rect.y = 30  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10  # how many pixels to move
eloc = []
eloc = [300, 0]
enemy_list = Level.bad(1, eloc)
gloc = []
tx = 64
ty = 64
i = 0
while i <= (worldx/tx)+tx:
    gloc.append(i*tx)
    i = i+1
ground_list = Level.ground(1, gloc, tx, ty)
plat_list = Level.platform(1, tx, ty)

'''
Main loop
'''

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
                player.jump()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)

            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps, 0)

            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

    # Scroll the world forward
    if player.rect.x >= forwardx:
        scroll = player.rect.x - forwardx
        player.rect.x = forwardx
        for p in plat_list:
            p.rect.x -= scroll
        for e in enemy_list:
            e.rect.x -= scroll

    # scroll the world backward
    if player.rect.x <= backwardx:
        scroll = backwardx - player.rect.x
        player.rect.x = backwardx
        for p in plat_list:
            p.rect.x += scroll
        for e in enemy_list:
            e.rect.x += scroll
    player.gravity()            # check gravity
    player.update()             # update player position
    world.blit(backdrop, backdropbox)
    player_list.draw(world)     # Draw player
    enemy_list.draw(world)      # refresh enemy
    ground_list.draw(world)     # refresh ground
    plat_list.draw(world)       # refresh platform
    for e in enemy_list:
        e.move()
    pygame.display.flip()
    clock.tick(fps)

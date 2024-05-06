import pygame
import enemy, level, menu, random

pygame.init()

class Stickman():
    def __init__(self,index, x, y):
        self.index = index
        self.reset(x, y)



    def update(self, game_over):
        dx = 0
        dy = 0
        walk_cooldown = 2

        if game_over == 0:
            #get keypresses
            key = pygame.key.get_pressed()
            if self.index == 0:
                if key[pygame.K_UP] and self.jumped == False and self.in_air == False:
                    self.vel_y = -1
                    self.jumped = True
                if key[pygame.K_UP] == False:
                    self.jumped = False
                if key[pygame.K_LEFT]:
                    dx -= 5
                    self.counter += 1
                    self.direction = -1
                if key[pygame.K_RIGHT]:
                    dx += 5
                    self.counter += 1
                    self.direction = 1
                if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                    self.counter = 0
                    self.index = 0
                    if self.direction == 1:
                        self.image = self.images_right[self.index]
                    if self.direction == -1:
                        self.image = self.images_left[self.index]
            elif self.index == 1:
                if key[pygame.K_w] and self.jumped == False and self.in_air == False:
                    self.vel_y = -15
                    self.jumped = True
                if key[pygame.K_w] == False:
                    self.jumped = False
                if key[pygame.K_a]:
                    dx -= 5
                    self.counter += 1
                    self.direction = -1
                if key[pygame.K_d]:
                    dx += 5
                    self.counter += 1
                    self.direction = 1
                if key[pygame.K_a] == False and key[pygame.K_RIGHT] == False:
                    self.counter = 0
                    self.index = 0
                    if self.direction == 1:
                        self.image = self.images_right[self.index]
                    if self.direction == -1:
                        self.image = self.images_left[self.index]

            #handle animation
            if self.counter > walk_cooldown:
                self.counter = 0	
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]


            #add gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            #check for collision
            #self.in_air = True
            #for tile in world.tile_list:
                #check for collision in x direction
                #if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    #dx = 0
                #check for collision in y direction
                #if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    #check if below the ground i.e. jumping
                    #if self.vel_y < 0:
                        #dy = tile[1].bottom - self.rect.top
                        #self.vel_y = 0
                    #check if above the ground i.e. falling
                    #elif self.vel_y >= 0:
                        #dy = tile[1].top - self.rect.bottom
                        #self.vel_y = 0
                        #self.in_air = False

            #check for collision with enemies
            #if pygame.sprite.spritecollide(self, game.blob_group, False):
                #game_over = -1

            #check for collision with lava
            #if pygame.sprite.spritecollide(self, game.lava_group, False):
                #game_over = -1

            #check for collision with exit
            #if pygame.sprite.spritecollide(self, game.exit_group, False):
                #game_over = 1


            #update player coordinates
            self.rect.x += dx
            self.rect.y += dy


        elif game_over == -1:
            self.image = self.dead_image
            if self.rect.y > 200:
                self.rect.y -= 5

        #draw player onto screen
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

        return game_over
              

    def reset(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1, 2):
            img_right = pygame.image.load(f'assets/p{self.index + 1}moveright{num}.gif')
            img_right = pygame.transform.scale(img_right, (40, 80))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.dead_image = pygame.image.load(f'assets/p{self.index + 1}standstill.gif')
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True
class Game():

    def main(self):
        global clock,FPS
        self.running = True
        self.enemies = []
        self.keys = pygame.key.get_pressed()
        self.player1 = Stickman(0, 50, 200)
        self.player2 = Stickman(1, 100, 200)
        # Spawn positions for players 1 and 2
        for x in range(0, 7):
            self.enemies.append(enemy.Enemy(x, 100 * x, 200))
        self.platformarr = [level.Platform(100, 205, 0)]
        while self.running:
            screen.fill((255, 255, 255))
            self.keys = pygame.key.get_pressed()
            self.player1.update(False)
            self.player2.update(False)
            self.hits = pygame.sprite.spritecollide(self.player1, self.platformarr, False)
            if self.hits:
                self.player1.pos.y = self.hits[0].rect.top
            # Update the display
            pygame.display.update()
            clock.tick(FPS)

game = Game()
# Font used to display the score and other information
font = pygame.font.Font("freesansbold.ttf", 40)

# Creating and setting screen width and height, display caption
WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
surf = pygame.Surface((WIDTH,HEIGHT))
pygame.display.set_caption("Stickman")

# Setting the clock object and fps
clock = pygame.time.Clock()
FPS = 60





if __name__ == "__main__":
    game.main()
    pygame.quit()

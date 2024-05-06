import pygame
import character, enemy, level, menu, random

pygame.init()

class Game():

    def main(self):
        self.running = True
        self.enemies = []
        self.keys = pygame.key.get_pressed()
        self.player1 = character.Stickman(0, 50, 200,self.keys)
        self.player2 = character.Stickman(1, 100, 200,self.keys)
        # Spawn positions for players 1 and 2
        for x in range(0, 7):
            self.enemies.append(enemy.Enemy(x, 100 * x, 200))
        self.platformarr = [level.Platform(100, 205, 0)]

        self.allsprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.allsprites.add(self.player1, self.player2)
        self.allsprites.add(self.enemies)
        while self.running:
            screen.fill((255, 255, 255))
            self.keys = pygame.key.get_pressed()
            self.player1.keys = self.keys
            self.player2.keys = self.keys
            self.allsprites.update()
            self.platforms.update()
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
character.__init__(WIDTH, HEIGHT, screen,game)
enemy.__init__(screen, WIDTH, HEIGHT)
level.__init__(WIDTH, HEIGHT, screen)
# Setting the clock object and fps
clock = pygame.time.Clock()
FPS = 60





if __name__ == "__main__":
    game.main()
    pygame.quit()

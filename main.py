import pygame,random,character,enemy,level,menu
pygame.init()

# Font used to display the score and other information
font = pygame.font.Font('freesansbold.ttf', 40)

# Creating and setting screen width and height, display caption
WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption("Stickman")

# Setting the clock object and fps
clock = pygame.time.Clock() 
FPS = 60


player1 = character.Stickman(0,50,200)
player2 = character.Stickman(1,100,200)
# Spawn positions for players 1 and 2

<<<<<<< Updated upstream
allsprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
allsprites.add(player1,player2)
=======
# Create the enemies for the players to fight
nonplayer = enemy.Enemy(0,200,200)
nonplayer = enemy.Enemy(1,300,100)
nonplayer = enemy.Enemy(2,500,100)
nonplayer = enemy.Enemy(3,700,200)
nonplayer = enemy.Enemy(4,900,100)
nonplayer = enemy.Enemy(5,300,200)
nonplayer = enemy.Enemy(6,900,200)
nonplayer = enemy.Enemy(7,700,100)
nonplayer = enemy.Enemy(8,500,200)

>>>>>>> Stashed changes

def main():
    running = True
    while running:
        
        # Update the display
          pygame.display.update()
          clock.tick(FPS)	
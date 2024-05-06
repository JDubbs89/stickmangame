import pygame, random, character, enemy, level, menu

pygame.init()

# Font used to display the score and other information
font = pygame.font.Font("freesansbold.ttf", 40)

# Creating and setting screen width and height, display caption
WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Stickman")
character.__init__(WIDTH, HEIGHT, screen)
enemy.__init__(screen, WIDTH, HEIGHT)
level.__init__(WIDTH, HEIGHT, screen)
# Setting the clock object and fps
clock = pygame.time.Clock()
FPS = 60

enemies = []
player1 = character.Stickman(0, 50, 200)
player2 = character.Stickman(1, 100, 200)
# Spawn positions for players 1 and 2
for x in range(0, 7):
    enemies.append(enemy.Enemy(x, 100 * x, 200))
platformarr = [level.Platform(100, 205, 0)]

allsprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
allsprites.add(player1, player2)
allsprites.add(enemies)


def main():
    global enemies, player1, player2, platformarr, allsprites, platforms
    running = True
    enemies = []
    player1 = character.Stickman(0, 50, 200)
    player2 = character.Stickman(1, 100, 200)
    # Spawn positions for players 1 and 2
    for x in range(0, 7):
        enemies.append(enemy.Enemy(x, 100 * x, 200))
    platformarr = [level.Platform(100, 205, 0)]

    allsprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    allsprites.add(player1, player2)
    allsprites.add(enemies)
    while running:
        screen.fill((255, 255, 255))
        allsprites.update()
        platforms.update()
        hits = pygame.sprite.spritecollide(player1, platformarr, False)
        if hits:
            player1.pos.y = hits[0].rect.top
        # Update the display
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()

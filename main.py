import pygame
from constants import *
from player import Player
def main():
    pygame.init()
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")

    clock = pygame.time.Clock()
    dt = clock.tick(60) / 1000

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        



if __name__ == "__main__":
    main()

